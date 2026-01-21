import requests
import time


class PaoDeAcucarAPI:
    def __init__(self, term, results_per_page=12):
        self.term = term
        self.results_per_page = results_per_page
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        }
        self.url = "https://api.vendas.gpa.digital/pa/search/search"
        self.base_payload = {
            "allowRedirect": True,
            "customerPlus": True,
            "department": "ecom",
            "page": 1,
            "partner": "linx",
            "resultsPerPage": self.results_per_page,
            "sortBy": "relevance",
            "storeId": 461,
            "terms": self.term,
            "userHash": "8a6dbb31a71601f820552289a0a8e2c194322a99c905146918a11569c4c8f1ee",
        }

    def fetch_products(self):
        all_products = []
        page = 1
        while True:
            payload = self.base_payload.copy()
            payload["page"] = page
            payload["terms"] = self.term
            response = requests.post(self.url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            products = data.get("products", [])
            for product in products:
                extracted = self._extract_product(product)
                all_products.append(extracted)
            total_pages = data.get("totalPages", 1)
            if page >= total_pages:
                break
            page += 1
            time.sleep(1)  # Respectful delay between requests
        return all_products

    def _extract_product(self, product):
        promo = product.get("productPromotion") or {}
        return {
            "stock": product.get("stock"),
            "priceType": product.get("priceType"),
            "price": product.get("price"),
            "brand": product.get("brand"),
            "name": product.get("name"),
            "sellerName": product.get("sellerName"),
            "sellType": product.get("sellType"),
            "priceFrom": product.get("priceFrom"),
            "url": product.get("urlDetails"),
            "promotionQuantityBuy": promo.get("promotionQuantityBuy"),
            "promotionQuantityPayFor": promo.get("promotionQuantityPayFor"),
            "startDate": promo.get("startDate"),
            "endDate": promo.get("endDate"),
            "unitPrice": promo.get("unitPrice"),
            "promotionPercentOff": promo.get("promotionPercentOff"),
        }


if __name__ == "__main__":
    api = PaoDeAcucarAPI("cafe")
    products = api.fetch_products()
    print(f"Total products fetched: {len(products)}")
    if products:
        print("Sample product:", products[0])
    else:
        print("No products found")
