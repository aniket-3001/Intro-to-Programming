import csv
import json


jsonArray = []
with open("IP TUTS/TUT-8/Extra/data.csv") as f1:
    for row in csv.DictReader(f1):
        jsonArray.append(row)


with open("IP TUTS/TUT-8/Extra/json_data.csv", 'w') as f2:
    f2.write(json.dumps(jsonArray))
    print("written to file successfully")
