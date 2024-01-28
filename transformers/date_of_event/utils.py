"""utils for date_of_event"""
import csv
from typing import Literal


def check_is_date_holiday(date: str, holidays: dict[str, str]) -> Literal[0, 1]:
    """if there's a holiday on the date, return 1, otherwise 0"""
    return 1 if holidays.get(date) else 0


def read_dict_data_from_csv_file(file_name) -> dict[str, str]:
    """read data from csv file and return it as a dictionary"""
    dict_from_csv = {}

    with open(f"data/{file_name}.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            dict_from_csv[row["key"]] = row["value"]

    return dict_from_csv
