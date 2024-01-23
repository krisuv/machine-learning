""" Transform 'event_location_region' column """
from pandas import DataFrame
from data.col_names import Default_columns, Restructured_columns
from transformers.utils import transform_categorical_data


def transform_event_location_region(data_frame: DataFrame) -> None:
    """
    remove rows with missing event_location_region
    transform column into 'location_gaza_strip', 'location_west_bank' and 'location_israel' columns
    """
    data_frame.dropna(subset=[Default_columns.EVENT_LOCATION_REGION], inplace=True)

    transform_categorical_data(
        data_frame,
        column_name=Default_columns.EVENT_LOCATION_REGION,
        new_column_names={
            "West Bank": Restructured_columns.EVENT_LOCATION_WEST_BANK,
            "Gaza Strip": Restructured_columns.EVENT_LOCATION_GAZA_STRIP,
            "Israel": Restructured_columns.EVENT_LOCATION_ISRAEL,
        },
    )
