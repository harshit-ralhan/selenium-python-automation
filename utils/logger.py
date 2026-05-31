import logging
import os
from datetime import datetime
def get_logger(name="selenium-tests", browser="chrome",data_source="json"):
    logs_folder = f"logs/{browser}_{data_source}"
    os.makedirs(logs_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    log_file_name = f"{logs_folder}/log_{timestamp}.log"
    logger = logging.getLogger(name)
    if not logger.handlers:  
        # Prevent duplicate handlers
        handler = logging.FileHandler(log_file_name, mode="a", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger, log_file_name