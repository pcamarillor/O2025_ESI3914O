#!/bin/bash

# Configuration
SOURCE_DIR=$1 # Directory with original files
DEST_DIR=$2       # Directory where files will be copied
SLEEP_INTERVAL=2                      # Time between checks (in seconds)

# Create directories if they don't exist
mkdir -p "$SOURCE_DIR" "$DEST_DIR"

echo "Starting file copier: Monitoring $SOURCE_DIR every $SLEEP_INTERVAL seconds..."

# Main loop
while true; do
  # Copy all files from source to destination
  for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
      filename=$(basename "$file")
      cp "$file" "$DEST_DIR/$filename"
    fi
  done
  sleep "$SLEEP_INTERVAL"
done
