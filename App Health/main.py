import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("app_health.log")])

URL = "http://www.accuknox.com/"

try:
    response = requests.head(URL)
except Exception as e:
    logging.warning(f"The application {URL} is down. The application probably doesn't exist or unavailable or not responding.")
    print("The application is down. The application probably doesn't exist or unavailable or not responding.")
else:
    if response.status_code == 200:
        logging.info(f"The application {URL} is UP.") 
        print("The application is UP")
    else:
        logging.warning(f"The application {URL} is DOWN: HTTP response code {response.status_code}")
        print(f"The application is DOWN: HTTP response code {response.status_code}")
