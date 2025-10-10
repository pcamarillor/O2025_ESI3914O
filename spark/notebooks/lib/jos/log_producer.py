import os, json, time, random, datetime

LOG_DIR = "/opt/spark/work-dir/data/server_logs/"

# Valores para los logs
levels = ["INFO", "WARN", "ERROR"]
codes = [200, 404, 500]
messages = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error"
}

# Bucle para generar logs
while True:
    level = random.choice(levels)
    code = random.choice(codes)
    message = messages[code]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "timestamp": timestamp,
        "level": level,
        "code": code,
        "message": message
    }

    file_name = "log_" + str(int(time.time())) + ".json"
    file_path = os.path.join(LOG_DIR, file_name)

    with open(file_path, "w") as f:
        json.dump(log_entry, f)

    print("Archivo creado:", file_path)
    time.sleep(3)
