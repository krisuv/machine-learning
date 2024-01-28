import csv

def save_to_csv_file(file_name, data) -> None:
    if not data:
        print("No data to save.")
        return
    
    with open(f"../data/{file_name}.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["key", "value"])
        writer.writeheader()
        writer.writerows(data)
