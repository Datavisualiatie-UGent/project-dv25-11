#!/usr/bin/env python

# read the the gzipped csv file and convert to json
import gzip
import json
import csv
import sys

data = []
parsed_data = {}
with gzip.open("src/data/survey_results_public.csv.gz", "rt", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f, delimiter=",", quotechar='"')
    for row in csv_reader:
        for lang in row["LanguageAdmired"].split(";"):
            data.append(
                    {
                        "language": lang,
                        "type": "admired",
                        "devtype": row["DevType"],
                    }
                )
        for lang in row["LanguageWantToWorkWith"].split(";"):
            data.append(
                    {
                        "language": lang,
                        "type": "desired",
                        "devtype": row["DevType"],
                    }
                )

json.dump(data, sys.stdout)
