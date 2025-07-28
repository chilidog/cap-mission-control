# cap-mission-control
# 🛩️ CAP Mission Control Platform

Welcome to the official repository for the **CAP Mission Control Platform (MCP)** — an extensible framework built to support Civil Air Patrol training operations, drone telemetry, cadet attendance, and real-time mission planning.

---

## 🚀 About the Project

CAP MCP is engineered to streamline mission control workflows by integrating:
- 🧭 Dynamic planning via interactive dashboards
- 📡 Live drone telemetry with support for OpenIPC and Parrot ARSDK
- 🎓 Cadet attendance tracking via CAPID scans
- 🧑‍✈️ Multi-MCP coordination and fleet simulation
- 🗺️ Real-time mapping and telemetry visualization

All built with scalability, CAP compliance, and squadron efficiency in mind.

---

## 📁 Repository Structure

```text
cap-mission-control/
├── mcp-server/          # MCP logic, JSON-RPC handlers, drone SDKs
├── mission-dashboard/   # Streamlit UI for planning & telemetry mapping
├── scripts/             # Tools for attendance, signal routing, automation
├── data/                # Sample missions, CAPID logs, telemetry packets
├── config/              # Fleet settings, unit filters, airframe profiles
└── assets/              # Icons, maps, CAP-specific UI elements

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en).
