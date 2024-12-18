import logging
import os
from datetime import datetime

# set name of log file
LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# set log file path
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# make log folder
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s",
    level=logging.INFO,
)


