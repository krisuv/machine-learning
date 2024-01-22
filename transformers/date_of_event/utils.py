from typing import Literal
import csv


def check_is_date_holiday(date: str, holidays: dict[str, str]) -> Literal[0, 1]:
    """if there's a holiday on the date, return 1, otherwise 0"""
    print(date)
    if holidays.get(date):
        print(date, holidays[date])
    return 1 if holidays.get(date) else 0


def read_dict_data_from_csv_file(file_name) -> dict[str, str]:
    dict = {}

    with open(f"data/{file_name}.csv", "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            dict[row["key"]] = row["value"]

    return dict
