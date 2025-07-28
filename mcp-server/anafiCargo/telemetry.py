# telemetry.py
import time
import json
import random
from datetime import datetime

class TelemetryLogger:
    def __init__(self, log_path="telemetry_log.json"):
        self.log_path = log_path
        self.entries = []

    def log(self, altitude, signal_strength, gps_position, battery_percent):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "timestamp": timestamp,
            "altitude_m": altitude,
            "signal_db": signal_strength,
            "gps": gps_position,
            "battery_percent": battery_percent
        }
        self.entries.append(entry)
        print(f"[Telemetry] Logged: {entry}")
        self._persist()

    def _persist(self):
        with open(self.log_path, "w") as f:
            json.dump(self.entries, f, indent=2)

    def simulate(self, duration_sec=60, interval_sec=5):
        print("[Telemetry] Simulation started...")
        for _ in range(0, duration_sec, interval_sec):
            altitude = round(random.uniform(20.0, 60.0), 2)
            signal = random.randint(-80, -50)
            gps = {"lat": round(random.uniform(34.0, 35.0), 6), "lon": round(random.uniform(-118.0, -117.0), 6)}
            battery = random.randint(0, 100)
            self.log(altitude, signal, gps, battery)
            time.sleep(interval_sec)
        print("[Telemetry] Simulation finished.")