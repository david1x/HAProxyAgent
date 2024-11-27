import os
import logging
from datetime import datetime


def setup_logging(log_file):
    """Sets up logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def log_rotation(log_file, max_log_size, log_rotation_days):
    """Checks and rotates the log file if necessary."""
    if os.path.exists(log_file):
        file_size = os.path.getsize(log_file)
        file_mod_time = os.path.getmtime(log_file)
        file_age_days = (datetime.now() - datetime.fromtimestamp(file_mod_time)).days

        if file_size >= max_log_size or file_age_days >= log_rotation_days:
            backup_name = f"{log_file}.{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
            os.rename(log_file, backup_name)
            logging.info(f"Log file rotated. Backup created: {backup_name}")

