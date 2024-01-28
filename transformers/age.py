from pandas import DataFrame
from data.col_names import DefaultColumns


def transform_age(data_frame: DataFrame) -> None:
    data_frame.dropna(subset=[DefaultColumns.AGE], inplace=True)
