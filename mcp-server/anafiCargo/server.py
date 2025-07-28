import json
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample CAP metadata tags
CAP_MISSION_ID = "CAP-TRN-ANA-002"
CAP_UNIT_CALLSIGN = "SER-FL-999"
TELEMETRY_STORE = []

# Command handler map
def launch_drone():
    # Simulate takeoff command
    print("Launching AnafiCargo...")
    return {"status": "launched", "timestamp": time.time()}

def move_to(coordinates):
    # Accepts dict: {"lat": float, "lon": float, "alt": int}
    print(f"Moving to {coordinates}...")
    TELEMETRY_STORE.append({
        "mission": CAP_MISSION_ID,
        "event": "moveTo",
        "coordinates": coordinates,
        "timestamp": time.time()
    })
    return {"status": "moving", "destination": coordinates}

def payload_drop():
    print("Initiating payload drop...")
    TELEMETRY_STORE.append({
        "mission": CAP_MISSION_ID,
        "event": "payload_drop",
        "timestamp": time.time()
    })
    return {"status": "payload_delivered"}

def get_telemetry():
    return TELEMETRY_STORE

# JSON-RPC listener
@app.route('/rpc', methods=['POST'])
def handle_rpc():
    try:
        data = request.get_json()
        method = data.get("method")
        params = data.get("params", {})
        
        # CAP input sanitization & logging
        print(f"[CAP RPC] Received: {method}, Params: {params}")

        # Method dispatch
        if method == "launch":
            result = launch_drone()
        elif method == "moveTo":
            result = move_to(params)
        elif method == "payload_drop":
            result = payload_drop()
        elif method == "get_telemetry":
            result = get_telemetry()
        else:
            return jsonify({"error": "Unknown method"}), 400

        return jsonify({"result": result})
    
    except Exception as e:
        print(f"RPC Error: {e}")
        return jsonify({"error": str(e)}), 500

# Entry point
if __name__ == '__main__':
    print(f"🚁 MCP AnafiCargo server starting...")
    app.run(host='0.0.0.0', port=5000)