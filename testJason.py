import json
# this is a json string (simulating a log entry
import psutil
from datetime import datetime 
import os
def log_system_stats(filename="system_logs.json"):
    stats = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "disk_stat": psutil.disk_io_counters()
    }

    with open(filename, "w") as file:
        json.dump(stats, file, indent=4)

    print("System stats logged successfully.")

log_system_stats()

