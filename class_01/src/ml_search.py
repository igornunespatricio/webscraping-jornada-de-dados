import requests
from bs4 import BeautifulSoup
import pandas as pd

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
headers = {"User-Agent": user_agent}

keyword = "sabonete"
url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    items = soup.find_all("div", {"class": "poly-card__content"})

    for item in items:
        title_tag = item.find("h3", {"class": "poly-component__title-wrapper"})
        title = title_tag.get_text(strip=True) if title_tag else ""
        rate_tag = item.find("span", {"class": "poly-phrase-label"})
        rate = rate_tag.get_text(strip=True) if rate_tag else ""
        link_tag = item.find("a", {"class": "poly-component__title"})
        link = link_tag["href"] if link_tag else ""
        previous_price_tag = item.find("s", {"class": "andes-money-amount--previous"})
        previous_price = (
            previous_price_tag.get_text(strip=True) if previous_price_tag else ""
        )
        current_price_tag = item.find(
            "span", {"class": "andes-money-amount--cents-superscript"}
        )
        current_price = (
            current_price_tag.get_text(strip=True) if current_price_tag else ""
        )
        seller_tag = item.find("span", {"class": "poly-component__seller"})
        seller = seller_tag.get_text(strip=True) if seller_tag else ""
        data.append(
            {
                "link": link,
                "title": title,
                "previous_price": previous_price,
                "current_price": current_price,
                "rate": rate,
                "seller": seller,
            }
        )

else:
    print("error")
