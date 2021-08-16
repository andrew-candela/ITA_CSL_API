import sys
from searcher.lib.searcher import fuzzy_name_search
from searcher.lib.io import write_csv_results, get_fuzzy_names
from typing import Iterable, Dict, Any


file_with_names = sys.argv[1]
outfile = sys.argv[2]


def get_results() -> Iterable[Dict[str, Any]]:

    for name in get_fuzzy_names(file_with_names):
        print(f"searching for {name}..")
        yield from fuzzy_name_search(name)


def main():
    write_csv_results(get_results(), outfile)


if __name__ == "__main__":
    main()
