import requests
import logging
import time
from requests.exceptions import RequestException, HTTPError

from utils.config import logger

MAX_RETRIES = 3
RETRY_STATUS_CODES = [500, 502, 503, 504]


def make_outbound_request(method, url, user_context=None, **kwargs):
    """
    Logs outbound requests with retries and error handling.
    can be used inside class-based methods for full control.
    """
    attempt = 0
    while attempt < MAX_RETRIES:
        attempt += 1
        try:
            start_time = time.time()
            response = requests.request(method, url, **kwargs)
            print(response.json(), "resp")
            elapsed = round(time.time() - start_time, 2)

            log_data = {
                "attempt": attempt,
                "method": method,
                "url": url,
                "status": response.status_code,
                "elapsed_time": f"{elapsed}s",
                "user": user_context,
            }

            logger.info(f"[OUTBOUND] {log_data}")

            if response.status_code in RETRY_STATUS_CODES:
                logger.warning(f"[RETRY] {response.status_code} for {url}")
                time.sleep(1)
                continue

            if response.status_code >= 400:
                logger.error(
                    f"[FAILURE] Non-retryable status {response.status_code} from {url}"
                )
                response.raise_for_status()

            return response

        except HTTPError as e:
            logger.error(f"[ERROR] HTTPError: {e}")
            raise e

        except RequestException as e:
            print("HTETK")
            logger.error(f"[ERROR] Attempt {attempt} failed for {url}: {str(e)}")

            if attempt == MAX_RETRIES:
                raise Exception(f"Failed after {MAX_RETRIES} attempts: {str(e)}")
            time.sleep(1)
