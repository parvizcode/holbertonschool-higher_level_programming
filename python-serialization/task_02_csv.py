import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)  # CSV-dən dict-lər siyahısı alırıq

        with open('data.json', mode='w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
