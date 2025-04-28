#!/usr/bin/env python

# read the the gzipped csv file and convert to json
import gzip
import json
import csv
import sys


# fields wanted
# - CompTotal
# - YearsCode
# - DevType

data = []
parsed_data = {}
with gzip.open("src/data/survey_results_public.csv.gz", "rt", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f, delimiter=",", quotechar='"')
    for row in csv_reader:
        # parse the data
        d = {
            "CompTotal": row["CompTotal"],
            "YearsCode": row["YearsCode"],
            "DevType": row["DevType"],
        }
        # add the data to the list
        data.append(d)

json.dump(data, sys.stdout)
