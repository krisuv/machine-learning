from pandas import DataFrame
from data.col_names import Default_columns

def transform_age(data_frame: DataFrame) -> None:
    data_frame.dropna(subset=[Default_columns.AGE], inplace=True)
