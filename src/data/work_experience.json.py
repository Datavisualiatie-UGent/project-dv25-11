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
        for lang in row["LanguageAdmired"].split(";"):
            if lang not in parsed_data:
                parsed_data[lang] = {
                    "admired": 0,
                    "desired": 0,
                }
            parsed_data[lang]["admired"] += 1
        for lang in row["LanguageWantToWorkWith"].split(";"):
            if lang not in parsed_data:
                parsed_data[lang] = {
                    "admired": 0,
                    "desired": 0,
                }
            parsed_data[lang]["desired"] += 1
