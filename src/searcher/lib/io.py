from typing import Iterable, Dict, Any
import json


def get_fuzzy_names(path: str) -> Iterable[str]:
    with open(path, "r") as name_file:
        for name in name_file.readlines():
            yield name.strip()


def write_json_results(results: Iterable[Dict[str, Any]], path: str) -> None:
    with open(path, "w") as outfile:
        for result in results:
            outfile.write(json.dumps(result))
