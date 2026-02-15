## Results

The AI-based IDS was executed on a simulated network traffic dataset.

The system successfully detected stealth anomalies using multi-feature scoring:
- Packet rate
- Connection count
- Failed login attempts

Detected suspicious IPs:
- 172.16.0.4
- 192.168.1.9
- 192.168.1.12

Each detection produced an anomaly score ≥ 2, indicating stealth intrusion behaviour.

Alerts were generated in real time and stored in the log file.
