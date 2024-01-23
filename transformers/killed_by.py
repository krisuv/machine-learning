from pandas import DataFrame
from data.col_names import Default_columns, Restructured_columns
from transformers.utils import transform_categorical_data


def transform_killed_by(data_frame: DataFrame) -> None:
    data_frame.dropna(columns=[Default_columns.KILLED_BY], inplace=True)

    transform_categorical_data(
        data_frame,
        column_name=Default_columns.KILLED_BY,
        new_column_names={
            "Israeli security forces": Restructured_columns.KILLED_BY_IDF,
            "Palestinian civilians": Restructured_columns.KILLED_BY_PALESTINIAN,
            "Israeli civilians": Restructured_columns.KILLED_BY_ISRAELI_CIVILIAN,
        },
    )
