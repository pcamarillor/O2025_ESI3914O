import os
import time
import random
from datetime import datetime

# --- Configuration ---
LOG_DIR = "/opt/spark/work-dir/data/logs/"
LOG_LEVELS = ["INFO", "WARN", "ERROR"]
SERVER_NODES = ["server-node-1", "server-node-2", "server-node-3", "server-node-4"]

MESSAGES = {
    "INFO": ["User login successful", "Data export completed"],
    "WARN": ["Disk usage 85%", "High CPU load detected"],
    "ERROR": [
        "404 Not Found",
        "500 Internal Server Error",
        "Database connection failed",
        "500 Service Unavailable"
    ]
}

def _generate_single_log_entry():
    """Generates a single, randomized log entry string."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_level = random.choices(LOG_LEVELS, weights=[0.6, 0.2, 0.2], k=1)[0]
    server_id = random.choice(SERVER_NODES)
    message = random.choice(MESSAGES[log_level])
    return f"{timestamp} | {log_level} | {message} | {server_id}"

def generate_log_files(num_files: int):
    """
    Generates a specified number of log files in the target directory.
    
    Args:
        num_files (int): The total number of log files to create.
    """
    if num_files <= 0:
        print("Number of files must be positive. No logs generated.")
        return
        
    print(f"Generating {num_files} log files in '{LOG_DIR}'...")
    os.makedirs(LOG_DIR, exist_ok=True)
    
    for i in range(num_files):
        log_line = _generate_single_log_entry()
        
        # Ensure a unique filename
        timestamp_ms = int(time.time() * 1000)
        file_path = os.path.join(LOG_DIR, f"log_{timestamp_ms}_{i}.log")
        
        with open(file_path, 'w') as f:
            f.write(log_line + "\n")
        
        # Small delay to ensure filenames are unique if generated very quickly
        time.sleep(0.01)
        
    print(f"Successfully generated {num_files} log files.")
