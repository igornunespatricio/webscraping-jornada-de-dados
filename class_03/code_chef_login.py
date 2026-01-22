import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
payload = {"name": EMAIL, "pass": PASSWORD, "form_id": "ajax_login_form"}
login_url = "https://www.codechef.com/api/codechef/login"

with requests.Session() as s:
    context = s.get(login_url, headers=headers)
    soup = BeautifulSoup(context.content, "html.parser")
    # needs to match the csrf token using lambda function because it has scape characters
    csrf_token = (
        soup.find("input", attrs={"name": lambda x: x and "csrfToken" in x})
        .get("value")
        .replace('\\"', "")
    )
    form_build_id = (
        soup.find("input", attrs={"name": lambda x: x and "form_build_id" in x})
        .get("value")
        .replace('\\"', "")
    )
    payload["csrfToken"] = csrf_token
    payload["form_build_id"] = form_build_id
    print("oi")
    response = s.post(login_url, data=payload, headers=headers)
    if response.status_code == 200:
        dashboard = s.get(
            "https://www.codechef.com/api/learn/dashboard", headers=headers
        )
        print(dashboard.content)
    else:
        print("Login failed")
