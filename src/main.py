import csv
from datetime import datetime

LOG_FILE = "logs/alerts.log"
DATASET_FILE = "datasets/network_traffic.csv"

# simple baseline for normal behaviour
NORMAL_PACKET_RATE = 20
NORMAL_CONN_COUNT = 10
NORMAL_FAILED_LOGINS = 1

def log_alert(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

def anomaly_score(packet):
    score = 0

    if int(packet["packet_rate"]) > NORMAL_PACKET_RATE:
        score += 1
    if int(packet["connection_count"]) > NORMAL_CONN_COUNT:
        score += 1
    if int(packet["failed_logins"]) > NORMAL_FAILED_LOGINS:
        score += 1

    return score

def detect_stealth(packet):
    score = anomaly_score(packet)

    # stealth attacks have small deviations across multiple features
    if score >= 2:
        return f"Stealth anomaly detected from {packet['ip']} (score={score})"
    return None

def run_ids():
    with open(DATASET_FILE, "r") as file:
        reader = csv.DictReader(file)

        for packet in reader:
            alert = detect_stealth(packet)

            if alert:
                print("[ALERT]", alert)
                log_alert(alert)

if __name__ == "__main__":
    run_ids()
