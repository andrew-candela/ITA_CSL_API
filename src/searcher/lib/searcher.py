import requests
from typing import Dict, Any
import os

CSL_ENDPOINT = "https://api.trade.gov/gateway/v1/consolidated_screening_list/search"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('ITA_API_KEY')}",
}


def fuzzy_name_search(name: str) -> Dict[str, Any]:
    params = {"fuzzy_name": name}
    resp = requests.get(CSL_ENDPOINT, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()
