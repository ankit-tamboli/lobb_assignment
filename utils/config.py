import logging
import os
from dotenv import load_dotenv

# LOGGER CONFIG START
LOG_DIR = "logs"
LOG_FILE = "outbound_requests.log"

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("outbound_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE))
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Avoid adding multiple handlers if reimported
if not logger.handlers:
    logger.addHandler(file_handler)

# Future: We can also add handlers here to push logs to CloudWatch, Loki, Datadog, database etc.
# e.g. logger.addHandler(CloudWatchHandler(...))

# LOGGER CONFIG END

# ENV CONFIG START

load_dotenv() 

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not LASTFM_API_KEY or not OPENWEATHER_API_KEY:
    raise ValueError("Missing API keys in environment variables.")

# ENV CONFIG END
