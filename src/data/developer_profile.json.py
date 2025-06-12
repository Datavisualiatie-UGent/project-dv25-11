#! /usr/bin/env python

# - `country` field
#- `DevType` field
#- custom `count` field
#- custom `total` field

# read the the gzipped csv file and convert to json
import gzip
import json
import csv
import sys

data = []
with gzip.open("src/data/survey_results_public.csv.gz", "rt", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f, delimiter=",", quotechar='"')
    for row in csv_reader:
        d = {
            "Country": row["Country"],
            "DevType": row["DevType"],
        }
        data.append(d)
json.dump(data, sys.stdout)
