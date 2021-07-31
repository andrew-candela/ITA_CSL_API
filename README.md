
# Search the CSL from trade.gov

Use an API like a civilized person.

You need to do the following to get a valid API token:

1. Register an account with trade.gov
2. Create an 'application' to generate an access token
3. Subscribe to the CSL API
4. Record the value of the API key you generated in step #2 into the `.env` file

## Setting up your environment

Once you have your token, you need to populate it into an environment variable.
This library expects the env variable to be called `ITA_API_KEY`.
If you're on a unix like system, running `source .env` will take care of this for you.

Now you can do the normal python dance:

1. create a virtual env `python3 -m venv venv`
2. install the dependencies `pip install -r requirements.txt`
3. install this package `pip install -e .`

## Using the API

This package can be invoked as follows:

```shell
python src/searcher/get_data.py names.txt output_file_name.jsonl
```

This will read in the names you want to search for in `names.txt`
and write the API results into `output_file_name.jsonl`.

The API results are [jsonlines](https://jsonlines.org/).
Each line of the file is a valid JSON wad, and each one can be parsed independantly.
If you're on a unix system, you can inspect the n'th line of files like this with

```shell
the_line_number_you_want=1
head -n $the_line_number_you_want | jq .
```

using the great [jq](https://stedolan.github.io/jq/) package.
