import csv

def save_to_csv_file(file_name, data, fieldnames):
    with open(f"data/{file_name}.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read_dict_data_from_csv_file(file_name) -> dict[str, str]:
    holidays_dict = {}

    with open(f"data/{file_name}.csv", "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            holidays_dict[row["date"]] = row["name"]

    return holidays_dict
