""" Transform 'date_of_event' column """
from pandas import DataFrame
from data.col_names import DefaultColumns, TransformedColumns
from .utils import check_is_date_holiday, read_dict_data_from_csv_file


def transform_date_of_event(data_frame: DataFrame) -> None:
    """
    remove rows with missing citizenship or other than
    transform column into 'is_israeli' and 'is_palestinian' columns
    """
    data_frame.dropna(subset=[DefaultColumns.DATE_OF_EVENT], inplace=True)
    data_frame[DefaultColumns.DATE_OF_EVENT] = data_frame[
        DefaultColumns.DATE_OF_EVENT
    ].dt.strftime("%Y-%m-%d")

    jewish_holidays = read_dict_data_from_csv_file("jewish_holidays")

    islamic_holidays = read_dict_data_from_csv_file("islamic_holidays")

    data_frame[TransformedColumns.DATE_JEWISH_HOLIDAY] = data_frame[
        DefaultColumns.DATE_OF_EVENT
    ].apply(check_is_date_holiday, args=(jewish_holidays,))

    data_frame[TransformedColumns.DATE_ISLAMIC_HOLIDAY] = data_frame[
        DefaultColumns.DATE_OF_EVENT
    ].apply(check_is_date_holiday, args=(islamic_holidays,))

    data_frame.drop(columns=[DefaultColumns.DATE_OF_EVENT], axis=1, inplace=True)
