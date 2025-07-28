import pytest
from anafiCargo import utils

def test_format_telemetry(telemetry_sample):
    formatted = utils.format_telemetry(telemetry_sample)
    assert formatted["drone_id"] == telemetry_sample["drone_id"]
    assert isinstance(formatted["timestamp"], str)
    assert formatted["altitude_m"] == round(telemetry_sample["altitude_m"], 2)
    assert formatted["gps_fix"] == telemetry_sample["gps_fix"]

def test_verify_capid(valid_capid, invalid_capid):
    assert utils.verify_capid(valid_capid) is True
    assert utils.verify_capid(invalid_capid) is False

def test_haversine_distance_accuracy(nearby_coords):
    lat1, lon1 = nearby_coords[0]
    lat2, lon2 = nearby_coords[1]
    dist = utils.haversine_distance(lat1, lon1, lat2, lon2)
    assert dist > 0
    assert isinstance(dist, float)

def test_is_within_tolerance_true(nearby_coords):
    assert utils.is_within_tolerance(*nearby_coords, tolerance_m=2.0) is True

def test_is_within_tolerance_false(distant_coords):
    assert utils.is_within_tolerance(*distant_coords, tolerance_m=2.0) is False
