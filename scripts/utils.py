import csv

def save_to_csv_file(file_name, data):
    with open(f"data/{file_name}.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["key", "value"])
        writer.writeheader()
        writer.writerows(data)
