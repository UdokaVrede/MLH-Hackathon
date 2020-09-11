import os
from dotenv import load_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
RADAR_LIVE_SECRET_SERVER = os.getenv("RADAR_LIVE_SECRET_SERVER")
RADAR_LIVE_CLIENT = os.getenv("RADAR_LIVE_CLIENT")

RADAR_TEST_SECRET_SERVER = os.getenv("RADAR_TEST_SECRET_SERVER")
RADAR_TEST_CLIENT = os.getenv("RADAR_TEST_CLIENT")
