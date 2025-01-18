import requests
import time
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Read username and password from environment variables
username = os.getenv("id")
password = os.getenv("password")

print(username)
print(password)


r = requests.post("http://172.16.0.30:8090/login.xml", data={"mode": 191, "username": f"{username}", "password": f"{password}", "a": time.time(), "producttype": 0})