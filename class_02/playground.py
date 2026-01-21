import time
import requests
from bs4 import BeautifulSoup
from pda_requests import PaoDeAcucarAPI

# Test the new class
api = PaoDeAcucarAPI("cafe")
products = api.fetch_products()
print(f"Total products fetched: {len(products)}")
if products:
    print("Sample product:", products[0])
else:
    print("No products found")
