import time
import random
from datetime import datetime, timedelta

BATCH_SIZE = 3
SLEEP_SECONDS = 10
STEP_MINUTES = 1

levels = ["INFO", "ERROR", "WARN"]

messages = {
    "INFO": [
        "Backup completed successfully",
        "New user registered",
        "Configuration saved",
    ],
    "ERROR": [
        "Database connection failed",
        "Unauthorized access attempt detected",
        "Service timeout while processing request",
    ],
    "WARN": [
        "CPU temperature high",
        "Low disk space on volume /dev/sda1",
        "Network latency above threshold",
    ],
}

nodes = ["node-1", "node-2", "node-3", "node-4", "node-5"]

print("Generando logs cada 10 segundos...\nPresiona Ctrl + C para detener.\n")

ts = datetime.now()
batch = 0

try:
    while True:
        filename = f"/opt/spark/work-dir/data/logs/log{batch}.log"
        lines = []

        for _ in range(BATCH_SIZE):
            lvl = random.choice(levels)
            msg = random.choice(messages[lvl])
            node = random.choice(nodes)
            stamp = ts.strftime("%Y-%m-%d %H:%M:%S")
            line = f"{stamp} | {lvl} | {msg} | {node}"
            print(line)
            lines.append(line)
            ts += timedelta(minutes=STEP_MINUTES)

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"\nSe generaron {BATCH_SIZE} logs en '{filename}'. Esperando {SLEEP_SECONDS} segundos...\n")
        batch += 1
        time.sleep(SLEEP_SECONDS)

except KeyboardInterrupt:
    print("\nPrograma interrumpido. Saliendo...")
