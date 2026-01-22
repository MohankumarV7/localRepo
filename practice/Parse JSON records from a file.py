#  Parse JSON records from a file
import json
with open("data.json","r") as f:
    for line in f:
        record = json.load(line)
        print(record)