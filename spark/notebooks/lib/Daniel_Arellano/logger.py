import random
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

states = ["INFO", "ERROR", "WARN"]

Descriptions = [["User login successful", "New Service Created Succesfully", "API Connected"],
["500 Internal Server Error", "404 Page Not Found", "503 System Temporarly Unavailable"],
["Disk usage 85%", "RAM usage below 90%", "1000k Requests in last 2 min"]]

Nodes = ["server-node-1", "server-node-2", "server-node-3"]

print("Generando grupos de logs cada 8 segundos...\nPresiona Ctrl + C para detener.")

TIMEZONE = ZoneInfo("America/Mexico_City")
tiempo_global = datetime.now(TIMEZONE)
batch_number = 0

try:
    while True:
        # Crear nombre de archivo con número de batch
        log_filename = f"/opt/spark/work-dir/data/lab7_logs/logs_batch_{batch_number}.log"

        with open(log_filename, "w", encoding="utf-8") as f:
            for i in range(5):
                state_int = random.randint(0, 2)
                state = states[state_int]

                desc_int = random.randint(0, 2)
                desc = Descriptions[state_int][desc_int]

                nodes_int = random.randint(0, 2)
                node = Nodes[nodes_int]

                fecha_formateada = tiempo_global.strftime("%Y-%m-%d %H:%M:%S")

                log_line = f"{fecha_formateada} | {state} | {desc} | {node}"

                print(log_line)
                if i < 4:
                    f.write(log_line + "\n")
                else:
                    f.write(log_line)

                # Avanza 5 minutos por cada log
                tiempo_global += timedelta(minutes=5)

        print(f"\n Se generaron 5 logs en '{log_filename}'. Esperando 8 segundos...\n")
        batch_number += 1
        time.sleep(8)

except KeyboardInterrupt:
    print("\n Programa detenido por el usuario.")
