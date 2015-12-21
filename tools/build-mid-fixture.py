import csv
import json

with open('built-mid-fixtures/mid-fixation-473-773.csv', 'r') as f:

    reader = csv.reader(f, delimiter=',')
    gazepoints = list(reader)[1:]  # omit the header

    a = []
    for gp in gazepoints:
        a.append([float(gp[0]), float(gp[1])])

    with open('built-mid-fixtures/mid-fixation-473-773.json', 'w') as jsonf:
        json.dump(a, jsonf)
