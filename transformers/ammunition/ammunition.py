"""This module contains the transformation logic for the ammunition data."""
from pandas import DataFrame
from data.col_names import DefaultColumns, TransformedColumns
from transformers.utils import transform_categorical_data
from .utils import format_ammunition_data


def transform_ammunition(data_frame: DataFrame) -> None:
    """transform ammunition data into new categories"""
    format_ammunition_data(data_frame)
    transform_categorical_data(
        data_frame,
        column_name=DefaultColumns.AMMUNITION,
        new_column_names={
            TransformedColumns.AMMUNITION_FIREARMS: TransformedColumns.AMMUNITION_FIREARMS,
            TransformedColumns.AMMUNITION_GROUND_EXPLOSIVES: TransformedColumns.AMMUNITION_GROUND_EXPLOSIVES,
            TransformedColumns.AMMUNITION_AIR_EXPLOSIVES: TransformedColumns.AMMUNITION_AIR_EXPLOSIVES,
            TransformedColumns.AMMUNITION_MELEE_WEAPONS: TransformedColumns.AMMUNITION_MELEE_WEAPONS,
            TransformedColumns.AMMUNITION_OTHER: TransformedColumns.AMMUNITION_OTHER,
        },
    )
