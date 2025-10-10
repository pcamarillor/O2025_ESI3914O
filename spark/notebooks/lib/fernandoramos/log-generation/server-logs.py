#!/usr/bin/env python3

"""
Server Room Monitoring Log Generator
Generates JSON log files simulating server room environmental and status data
Compatible with Spark Structured Streaming
"""

import json
import random
import time
from datetime import datetime
import os
import sys

class ServerRoomLogGenerator:
    def __init__(self, output_dir="."):
        self.output_dir = output_dir
        self.server_ids = ["SERVER-001", "SERVER-002", "SERVER-003", "SERVER-004", "SERVER-005"]
        self.status_codes = [200, 200, 200, 200, 404, 500, 503]  # More 200s for realism
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"Output directory: {os.path.abspath(self.output_dir)}")
    
    def generate_log_entry(self):
        # Normal temperature range: 18-25°C, with occasional spikes
        base_temp = random.uniform(18, 25)
        # 10% chance of temperature alert
        if random.random() < 0.1:
            temperature = random.uniform(26, 32)  # High temperature alert
        else:
            temperature = base_temp
        
        # Normal humidity range: 40-60%, with occasional alerts
        base_humidity = random.uniform(40, 60)
        # 10% chance of humidity alert
        if random.random() < 0.1:
            humidity = random.uniform(65, 80)  # High humidity alert
        else:
            humidity = base_humidity
        
        # Status codes - 20% chance of error
        if random.random() < 0.2:
            status = random.choice([404, 500, 503])
        else:
            status = 200
        
        # Generate log entry - ensure all values are proper types
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "server_id": random.choice(self.server_ids),
            "temperature_celsius": round(temperature, 2),
            "humidity_percent": round(humidity, 2),
            "status_code": status,  
            "cpu_usage_percent": round(random.uniform(20, 95), 2),
            "power_watts": round(random.uniform(150, 450), 2)
        }
        
        return log_entry
    
    def generate_batch_file(self, num_entries=10):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  
        filename = f"server_logs_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        logs = []
        for _ in range(num_entries):
            logs.append(self.generate_log_entry())
            time.sleep(0.05)  # Small delay between entries
        
        # Write to file (one JSON object per line)
        with open(filepath, 'w') as f:
            for log in logs:
                json_line = json.dumps(log)
                f.write(json_line + '\n')
        
        return filepath
    
    def run_continuous(self, interval=5, entries_per_batch=10, max_batches=10):
        """
        Input arguments:
            interval: seconds between batch generation
            entries_per_batch: number of log entries per file
            max_batches: maximum number of batches 
        """
        
        batch_count = 0
        try:
            while max_batches is None or batch_count < max_batches:
                self.generate_batch_file(entries_per_batch)
                batch_count += 1
                
                if max_batches is None or batch_count < max_batches:
                    time.sleep(interval)

        except KeyboardInterrupt:
            return

def main():    
    # Default parameters
    output_dir = "."
    interval = 5
    entries_per_batch = 10
    max_batches = 10
    
    # Parse simple command-line arguments
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    if len(sys.argv) > 2:
        interval = int(sys.argv[2])
    if len(sys.argv) > 3:
        entries_per_batch = int(sys.argv[3])
    if len(sys.argv) > 4:
        max_batches = int(sys.argv[4])
    
    generator = ServerRoomLogGenerator(output_dir)
    generator.run_continuous(interval, entries_per_batch, max_batches)

if __name__ == "__main__":
    main()