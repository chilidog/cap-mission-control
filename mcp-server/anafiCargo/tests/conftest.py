import pytest
from datetime import datetime

@pytest.fixture
def telemetry_sample():
    return {
        "drone_id": "ANA-CARGO-01",
        "altitude_m": 72.4,
        "speed_mps": 15.12,
        "battery_pct": 93.0,
        "gps_fix": True,
        "timestamp": datetime.utcnow().isoformat()
    }

@pytest.fixture
def valid_capid():
    return "123456"

@pytest.fixture
def invalid_capid():
    return "abc123"

@pytest.fixture
def nearby_coords():
    return (27.00000, -80.00000), (27.00001, -80.00001)

@pytest.fixture
def distant_coords():
    return (27.00000, -80.00000), (27.01000, -80.01000)
