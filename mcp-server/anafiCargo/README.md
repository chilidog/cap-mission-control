# anafiCargo MCP Module

The `anafiCargo` mission control processor (MCP) module powers Civil Air Patrol (CAP) drone operations for cargo drop simulations and telemetry logging. It interfaces with Parrot's ARSDK and dispatches CAP-compliant missions using JSON-RPC protocols.

## 🧭 Overview

This module supports:

- Real-time telemetry parsing and dispatch formatting
- GPS tolerance checks and waypoint verification
- CAPID validation for training compliance
- Modular config loading for diverse mission profiles

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `pytest` for unit testing
- Parrot ARSDK bindings (local or remote)
- Parrot ARSDK bindings (local or remote)
- CAP unit deployment metadata

### Installation

```bash
git clone https://github.com/<your-org>/anafiCargo.git
cd anafiCargo
pip install -r requirements.txt
