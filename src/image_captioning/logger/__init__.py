import logging
import os
from datetime import datetime

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(BASE_DIR, "logs")

# Create logs directory
try:
    os.makedirs(logs_path, exist_ok=True)
except PermissionError:
    print(f"Permission denied creating {logs_path}, using /tmp/logs instead")
    logs_path = "/tmp/logs"
    os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)