""" Transform 'gender' column """
from pandas import DataFrame
from data.col_names import DefaultColumns, TransformedColumns
from transformers.utils import transform_categorical_data


def transform_gender(data_frame: DataFrame) -> None:
    """
    remove rows with missing gender
    transform column 'gender' into 'is_male' and 'is_female' columns
    """

    transform_categorical_data(
        data_frame,
        column_name=DefaultColumns.GENDER,
        new_column_names={
            "M": TransformedColumns.IS_MALE,
            "F": TransformedColumns.IS_FEMALE,
        },
    )
