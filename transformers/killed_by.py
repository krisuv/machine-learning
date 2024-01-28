""" Module for transforming the killed_by column of the data frame. """
from pandas import DataFrame
from data.col_names import DefaultColumns, TransformedColumns
from transformers.utils import transform_categorical_data


def transform_killed_by(data_frame: DataFrame) -> None:
    """Transform 'killed_by' column"""
    data_frame.dropna(subset=[DefaultColumns.KILLED_BY], inplace=True)

    transform_categorical_data(
        data_frame,
        column_name=DefaultColumns.KILLED_BY,
        new_column_names={
            "Israeli security forces": TransformedColumns.KILLED_BY_IDF,
            "Palestinian civilians": TransformedColumns.KILLED_BY_PALESTINIAN,
            "Israeli civilians": TransformedColumns.KILLED_BY_ISRAELI_CIVILIAN,
        },
    )
