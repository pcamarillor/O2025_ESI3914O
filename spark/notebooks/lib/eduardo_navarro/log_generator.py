import random 
import time 
import os
from datetime import datetime

logLevel = ["INFO", "WARN", "ERROR"]
httpCode = ["404 Not Found", "405 Method Not Allowed", "408 Request Timeout", "409 Conflict"]

fileInterval = 10
fileCount = 1

logDirectory = "./lab7Logs"
os.makedirs(logDirectory, exist_ok=True)

print("Iniciando generador de logs...")

try:
    while True:
        logFile = f"{logDirectory}/logs_batch_{fileCount}.log"
        logs_in_file = random.randint(2, 4)
        
        with open(logFile, 'w') as f:   
            for _ in range(logs_in_file):
                timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                level = random.choice(logLevel)
                code = random.choice(httpCode)
                logLine = f"{timeStamp}, {level}, {code}\n"
                f.write(logLine)
        
        print(f"Archivo #{fileCount} creado: {logFile} - {logs_in_file} logs generados")
        fileCount += 1
        time.sleep(fileInterval)

except KeyboardInterrupt:
    print(f"\nGenerador detenido. Total de archivos creados: {fileCount - 1}")