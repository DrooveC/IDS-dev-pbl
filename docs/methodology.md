
# Methodology

## 1. Data Collection
Since real-time packet capture was outside the scope of this implementation, a simulated network traffic dataset was used.  
Each traffic record represents a network flow with the following features:

- Packet rate
- Connection count
- Failed login attempts
- Port number
- Protocol type

These features were selected because they are commonly used indicators for stealth intrusion behaviour.

## 2. Data Preprocessing
The dataset was parsed using a CSV-based pipeline.  
Each record was converted into a structured feature vector for analysis.  
Missing or malformed entries were ignored to maintain data integrity.

## 3. Normal Behaviour Profiling
A baseline of normal network behaviour was defined using threshold values for:

- Packet rate
- Connection frequency
- Failed login attempts

This baseline represents legitimate traffic patterns and serves as a reference for anomaly detection.

## 4. Feature-Based Anomaly Scoring
For each network flow, an anomaly score was computed based on deviations from the normal baseline:

- High packet rate → score increment  
- High connection count → score increment  
- Excessive failed logins → score increment  

Stealth attacks typically exhibit small deviations across multiple features rather than a single large spike.  
Therefore, cumulative scoring was used to identify such behaviour.

## 5. Stealth Intrusion Detection
If the anomaly score exceeded a predefined threshold (score ≥ 2), the traffic was classified as a stealth intrusion.  
This approach allows detection of low-and-slow attacks that bypass traditional signature-based systems.

## 6. Alert Generation and Logging
When a stealth anomaly was detected:

- A real-time alert was displayed on the console  
- The event was recorded in a log file with timestamp and source IP  

This ensures traceability and supports forensic analysis.

## 7. Hybrid IDS Capability
In addition to anomaly detection, a signature repository was included for known attacks.  
Although not actively used in the current simulation, this supports a hybrid IDS architecture combining:

- Signature-based detection  
- AI/ML-based anomaly detection

## 8. Conceptual ML Mapping
The implemented anomaly scoring mechanism is conceptually aligned with unsupervised machine learning models such as:

- Isolation Forest  
- One-Class SVM  

These models identify deviations from normal patterns without requiring labelled attack data.

## 9. System Workflow
1. Input network traffic dataset  
2. Extract features  
3. Compute anomaly score  
4. Classify stealth intrusion  
5. Generate alert and log entry
