import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

log_file = f"logs/run_{run_id}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("financial_agent")

logger.info("Application started")