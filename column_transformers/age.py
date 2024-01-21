from pandas import DataFrame
from enums import Default_columns

def transform_age(data_frame: DataFrame) -> None:
    data_frame.dropna(subset=[Default_columns.AGE], inplace=True)
