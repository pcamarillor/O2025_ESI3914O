import requests
import os
import time
from datetime import datetime

# --- 1. Configuration ---

# The static URL for the Waze API endpoint
API_URL = "https://www.waze.com/row-partnerhub-api/partners/12985309755/waze-feeds/4376eba3-e054-434b-9369-0c2e65855416?format=1" 

# The HOST path for your Docker volume.
# This script saves files HERE, and Docker makes them appear
# inside the container at /opt/spark/work-dir/data/leon_mx_traffic/
SAVE_DIR = "C:/Users/akran/SYStop/!SYS-FALL2025/Big-Data/CLASS-REPO/O2025_ESI3914O/spark/data/leon_mx_traffic/"

# --- 2. Collection Settings ---
NUM_SAMPLES_TO_COLLECT = 68
POLL_INTERVAL_SECONDS = 120 # 2 minutes

# --- End of Configuration ---


def fetch_and_save_data():
    """
    Connects to the API, fetches data, and saves it to a timestamped JSON file.
    """
    
    # No Authorization header is needed; auth is in the URL.
    headers = {}
    
    print(f"Connecting to API at {API_URL}...")
    
    try:
        # Make the HTTP GET request
        response = requests.get(API_URL, headers=headers, timeout=10)
        
        # Raise an error if the request failed (e.g., 401, 404, 500)
        response.raise_for_status() 
        
        # --- File Saving ---
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"traffic_{timestamp}.json"
        filepath = os.path.join(SAVE_DIR, filename)
        
        # Write the raw JSON text to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
            
        print(f"  [SUCCESS] Saved sample to {filepath}")
        return True

    except requests.exceptions.HTTPError as http_err:
        print(f"  [HTTP ERROR] {http_err} - Check your URL and connection.")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"  [CONNECTION ERROR] {conn_err} - Check your internet connection.")
    except requests.exceptions.Timeout as timeout_err:
        print(f"  [TIMEOUT ERROR] The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"  [ERROR] An unknown error occurred: {err}")
        
    return False

def main():
    """
    Main function to run the data collection loop.
    """
    print("--- Starting Batch Data Collection ---")
    
    # Create the save directory on your Windows machine
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    for i in range(1, NUM_SAMPLES_TO_COLLECT + 1):
        print(f"\nFetching sample {i} of {NUM_SAMPLES_TO_COLLECT}...")
        
        success = fetch_and_save_data()
        
        if success and i < NUM_SAMPLES_TO_COLLECT:
            # If successful and not the last sample, wait.
            print(f"Waiting {POLL_INTERVAL_SECONDS} seconds for next poll...")
            time.sleep(POLL_INTERVAL_SECONDS)
        elif not success:
            # If it failed, stop the script.
            print("Stopping script due to data collection error.")
            break
            
    print("\n--- Batch Data Collection Complete ---")

if __name__ == "__main__":
    main()