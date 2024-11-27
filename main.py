import os
import time
import logger
import hashlib
import tester


# Folder path to monitor
FOLDER_PATH = r"/path/to/json/folder"
LOG_FILE = "haproxy-agent.log"
CHECK_INTERVAL = 8  # seconds between checks
LOG_ROTATION_DAYS = 30
MAX_LOG_SIZE = 2 * 1024 * 1024 * 1024  # 2GB in bytes 


def get_file_hash(file_path):
    """Returns the MD5 hash of the file content."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        buffer = f.read()
        hasher.update(buffer)
    return hasher.hexdigest()


def monitor_folder(folder_path):
    """Monitors a folder for new JSON files and processes them."""
    processed_files = set()  # Track processed file hashes

    while True:
        logger.log_rotation(log_file=LOG_FILE, max_log_size=MAX_LOG_SIZE, log_rotation_days=LOG_ROTATION_DAYS)  # Check if log rotation is needed
        found_new_file = False

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if file_name.endswith(".json") and os.path.isfile(file_path):
                file_hash = get_file_hash(file_path)

                if file_hash not in processed_files:
                    try:
                        with open(file_path, "r") as file:
                            file_content = tester.json.load(file)

                        logger.logging.info(f"New file detected: {file_name}")
                        print(f"New file detected: {file_name}")
                        tester.is_pass(file_content)
                        processed_files.add(file_hash)

                        os.remove(file_path)  # Delete the file after processing
                        logger.logging.info(f"File {file_name} processed and deleted.")
                        print(f"File {file_name} processed and deleted.")
                        found_new_file = True

                    except tester.json.JSONDecodeError:
                        logger.logging.error(f"Error: {file_name} is not a valid JSON file.")
                        print(f"Error: {file_name} is not a valid JSON file.")
                    except Exception as e:
                        logger.logging.error(f"Error processing {file_name}: {e}")
                        print(f"Error processing {file_name}: {e}")

        if not found_new_file:
            logger.logging.debug("No new JSON files detected.")
            print("No new JSON files detected.")

        time.sleep(CHECK_INTERVAL)



if __name__ == "__main__":
    logger.setup_logging(log_file=LOG_FILE)
    logger.logging.info("Starting HAProxy Agent...")
    monitor_folder(FOLDER_PATH)


