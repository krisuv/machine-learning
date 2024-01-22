""" Transform 'date_of_event' column """
from pandas import DataFrame
from enums import Default_columns, Restructured_columns
from .utils import check_is_date_holiday, read_dict_data_from_csv_file

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
