""" Transform 'gender' column """
from pandas import DataFrame
from data.col_names import Default_columns, Restructured_columns
from transformers.utils import transform_categorical_data


def transform_gender(data_frame: DataFrame) -> None:
    """
    remove rows with missing gender
    transform column into 'Male' and 'Female' columns
    """
    data_frame.dropna(subset=[Default_columns.GENDER], inplace=True)

    transform_categorical_data(
        data_frame,
        column_name=Default_columns.GENDER,
        new_column_names={
            "M": Restructured_columns.IS_MALE,
            "F": Restructured_columns.IS_FEMALE,
        },
    )
