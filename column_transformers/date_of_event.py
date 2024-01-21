""" Transform 'date_of_event' column """
from typing import Literal
from pandas import DataFrame
from enums import Default_columns, Restructured_columns
from utils.file_utils import read_dict_data_from_csv_file


def check_is_date_holiday(date: str, holidays: dict[str, str]) -> Literal[0, 1]:
    """if there's a holiday on the date, return 1, otherwise 0"""
    print(date)
    if holidays.get(date):
        print(date, holidays[date])
    return 1 if holidays.get(date) else 0


def transform_date_of_event(data_frame: DataFrame) -> None:
    """
    remove rows with missing citizenship or other than
    transform column into 'is_israeli' and 'is_palestinian' columns
    """
    data_frame.dropna(subset=[Default_columns.DATE_OF_EVENT], inplace=True)

    jewish_holidays = read_dict_data_from_csv_file("jewish_holidays")

    islamic_holidays = read_dict_data_from_csv_file("islamic_holidays")

    data_frame[Restructured_columns.DATE_JEWISH_HOLIDAY] = data_frame[
        Default_columns.DATE_OF_EVENT
    ].apply(check_is_date_holiday, args=(jewish_holidays,))

    data_frame[Restructured_columns.DATE_ISLAMIC_HOLIDAY] = data_frame[
        Default_columns.DATE_OF_EVENT
    ].apply(check_is_date_holiday, args=(islamic_holidays,))

    data_frame.drop(columns=[Default_columns.DATE_OF_EVENT], axis=1, inplace=True)
