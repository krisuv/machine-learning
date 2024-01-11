import csv
import json


def save_to_json_file(file_name, data):
    file = open(f"data/{file_name}.json", "w")
    file.write(json.dumps(data))
    file.close()


def save_to_csv_file(file_name, data, fieldnames):
    with open(f"data/{file_name}.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
