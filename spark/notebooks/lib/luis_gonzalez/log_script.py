#!/usr/bin/env python3
"""
Simple Server Log Generator - NO TIMESTAMPS
Generates random server logs for Lab 07
"""

import json
import random
import time
import os

LOG_DIR = "./logs/"

NUM_SERVERS = 5
LOGS_PER_FILE = 15
INTERVAL_SECONDS = 5

STATUS_CODES = [200] * 7 + [404] * 1 + [500] * 1 + [503] * 1

def generate_log_entry():
    """Generate a single simple log entry WITHOUT timestamp"""
    return {
        "server_id": f"SERVER-{random.randint(1, NUM_SERVERS):03d}",
        "status_code": random.choice(STATUS_CODES),
        "response_time_ms": round(random.uniform(50, 1000), 2),
        "cpu_usage": round(random.uniform(10, 95), 2),
        "memory_usage": round(random.uniform(20, 90), 2)
    }

def generate_log_file(file_number):
    """Generate a log file with multiple entries"""
    logs = [generate_log_entry() for _ in range(LOGS_PER_FILE)]
    
    os.makedirs(LOG_DIR, exist_ok=True)
        filename = f"{LOG_DIR}server_logs_{file_number:04d}.json"
    with open(filename, 'w') as f:
        for log in logs:
            f.write(json.dumps(log) + '\n')
    
    print(f"Generated: {filename} ({len(logs)} entries)")

def main():
    """Main function to continuously generate log files"""
    print("LOG GENERATOR STARTED")
    print(f"Directory: {os.path.abspath(LOG_DIR)}")
    print(f"Logs per file: {LOGS_PER_FILE}")
    print(f"Interval: {INTERVAL_SECONDS} seconds")
    print("=" * 60)
    
    file_number = 1
    
    try:
        while True:
            generate_log_file(file_number)
            file_number += 1
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n\Log generation stopped by user")

if __name__ == "__main__":
    main()