from pandas import DataFrame
from enums import Default_columns


def format_age(data_frame: DataFrame) -> None:
    data_frame = data_frame.dropna(subset=[Default_columns.AGE])
