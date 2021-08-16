import requests
from typing import Dict, Any, Iterable
from searcher.lib.format_record import format_result
import os

CSL_ENDPOINT = "https://api.trade.gov/gateway/v1/consolidated_screening_list/search"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('ITA_API_KEY')}",
}


def fuzzy_name_search(name: str) -> Iterable[Dict[str, Any]]:
    params = {"fuzzy_name": True, "name": name}
    resp = requests.get(CSL_ENDPOINT, headers=headers, params=params)
    resp.raise_for_status()
    yield from format_result(name, resp.json())
