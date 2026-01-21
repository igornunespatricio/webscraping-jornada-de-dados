import os
import requests
from dotenv import load_dotenv

load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
payload = {"email": EMAIL, "password": PASSWORD, "form_id": "ajax_login_form"}

response = requests.post(
    "https://www.codechef.com/api/codechef/login", data=payload, headers=headers
)
if response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")
