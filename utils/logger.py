import logging
import os
def get_logger(name="selenium-tests"):
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    if not logger.handlers:  
        # Prevent duplicate handlers
        handler = logging.FileHandler("logs/test_run.log", mode="a", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger