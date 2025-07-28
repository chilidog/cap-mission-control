import json
import math
from datetime import datetime

def format_telemetry(data):
    """Standardize telemetry payload for logging or dispatch"""
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "drone_id": data.get("drone_id", "UNKNOWN"),
        "altitude_m": round(data.get("altitude_m", 0), 2),
        "speed_mps": round(data.get("speed_mps", 0), 2),
        "battery_pct": round(data.get("battery_pct", 0), 1),
        "gps_fix": data.get("gps_fix", False),
    }

def verify_capid(capid):
    """Basic CAPID validation: must be numeric, 6 digits"""
    return str(capid).isdigit() and len(str(capid)) == 6

def load_config(path="config.json"):
    """Load JSON config file from disk"""
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"[ERROR] Config load failed: {e}")
        return {}

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two lat/lon coordinates (meters)"""
    R = 6371000  # Radius of Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def is_within_tolerance(coord1, coord2, tolerance_m):
    """Check if two GPS coordinates are within tolerance radius"""
    dist = haversine_distance(*coord1, *coord2)
    return dist <= tolerance_m
