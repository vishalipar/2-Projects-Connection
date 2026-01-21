import requests
from typing import List, Dict, Optional

class ProductAPIClient:
    BASE_URL = "http://localhost:8000/api/products/"
    
    @staticmethod
    def get_all_products() -> List[Dict]:
        """Fetch all products from Project 1"""
        try:
            response = requests.get(ProductAPIClient.BASE_URL)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products: {e}")
            return []
    
    @staticmethod
    def get_product(product_id: int) -> Optional[Dict]:
        """Fetch a single product by ID"""
        try:
            response = requests.get(f"{ProductAPIClient.BASE_URL}{product_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching product {product_id}: {e}")
            return None