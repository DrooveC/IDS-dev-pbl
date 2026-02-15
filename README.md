# AI-Based Intrusion Detection System for Stealth Attack Detection

## Problem Statement
Traditional signature-based IDS systems fail to detect stealthy and low-rate attacks that mimic normal traffic patterns.  
This project proposes an AI/ML-based Intrusion Detection System capable of identifying subtle anomalies in network behavior to detect stealth intrusions.

## Objectives
- Detect stealth attacks that bypass signature-based systems
- Use machine learning for anomaly detection
- Analyse network traffic features such as packet rate, port usage, and protocol distribution
- Generate real-time alerts and maintain logs of suspicious activity
- Reduce false negatives for low-and-slow attacks

## Proposed Approach
The system uses an anomaly detection model trained on normal traffic patterns.  
Incoming traffic is compared against this baseline to identify deviations.

Detection pipeline:
1. Traffic dataset input (simulated network flow)
2. Feature extraction (packet rate, port frequency, protocol behavior)
3. ML-based anomaly scoring
4. Threshold-based stealth intrusion detection
5. Alert generation and logging

## Type of IDS
Hybrid IDS:
- Signature-based detection for known attacks
- ML-based anomaly detection for stealth intrusions

## Tech Stack
- Python
- Scikit-learn (Isolation Forest / One-Class SVM – conceptual)
- CSV-based network traffic dataset
- Logging module for alert storage

## Dataset
A simulated network traffic dataset is used to represent normal and stealth attack patterns.  
Features include:
- Source IP
- Destination port
- Protocol
- Packet rate
- Connection frequency

## System Modules
- Data Preprocessing Module
- Feature Extraction Module
- ML Anomaly Detection Engine
- Signature Matching Engine
- Alert & Logging System

## How to Run
```bash
python src/main.py
