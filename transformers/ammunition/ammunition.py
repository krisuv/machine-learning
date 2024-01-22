from pandas import DataFrame
from enums import Default_columns, Restructured_columns
from transformers.utils import transform_categorical_data
from .utils import format_ammunition_data, get_missing_ammunition_from_notes


def transform_ammunition(data_frame: DataFrame) -> None:
    format_ammunition_data(data_frame)
    get_missing_ammunition_from_notes(data_frame)
    transform_categorical_data(
        data_frame,
        column_name=Default_columns.AMMUNITION,
        new_column_names={
            Restructured_columns.AMMUNITION_FIREARMS,
            Restructured_columns.AMMUNITION_GROUND_EXPLOSIVES,
            Restructured_columns.AMMUNITION_AIR_EXPLOSIVES,
            Restructured_columns.AMMUNITION_MELEE_WEAPONS,
            Restructured_columns.AMMUNITION_OTHER,
        },
    )
