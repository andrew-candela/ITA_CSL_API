from typing import Iterable, Dict, Any, Union
import json


outfile_headers = [
    "Searched Name",
    "Source",
    "Entity Number",
    "Type",
    "Name",
    "Score",
    "Source List URL",
    "Source Information URL",
    "Programs",
    "Addresses",
    "IDs",
]


def print_default_record(searched_name: str) -> Dict[str, Union[str, None]]:
    return {
        "Searched Name": searched_name,
        "Source": None,
        "Entity Number": None,
        "Type": None,
        "Name": None,
        "Score": None,
        "Source List URL": None,
        "Source Information URL": None,
        "Programs": None,
        "Addresses": None,
        "IDs": None,
    }


class ResultFields:
    total = "total"
    offset = "offset"
    results = "results"
    source = "source"
    entity_number = "entity_number"
    type = "type"
    name = "name"
    score = "score"
    source_list_url = "source_list_url"
    source_information_url = "source_information_url"
    programs = "programs"
    addresses = "addresses"
    ids = "ids"


def get_source(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.source)


def get_entity_number(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.entity_number)


def get_type(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.type)


def get_name(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.name)


def get_score(result_record: Dict[str, Any]) -> int:
    return result_record.get(ResultFields.score)


def get_source_list_url(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.source_list_url)


def get_source_information_url(result_record: Dict[str, Any]) -> str:
    return result_record.get(ResultFields.source_information_url)


def get_programs(result_record: Dict[str, Any]) -> str:
    return json.dumps(result_record.get(ResultFields.programs), indent=4)


def get_addresses(result_record: Dict[str, Any]) -> str:
    return json.dumps(result_record.get(ResultFields.addresses), indent=4)


def get_ids(result_record: Dict[str, Any]) -> str:
    return json.dumps(result_record.get(ResultFields.ids), indent=4)


def format_result(
    searched_name: str, search_result: Dict[str, Any]
) -> Iterable[Dict[str, str]]:
    if search_result.get("total", 0) == 0:
        yield print_default_record(searched_name)
    for result in search_result.get("results"):
        yield {
            "Searched Name": searched_name,
            "Source": get_source(result),
            "Entity Number": get_entity_number(result),
            "Type": get_type(result),
            "Name": get_name(result),
            "Score": get_score(result),
            "Source List URL": get_source_list_url(result),
            "Source Information URL": get_source_information_url(result),
            "Programs": get_programs(result),
            "Addresses": get_addresses(result),
            "IDs": get_ids(result),
        }
