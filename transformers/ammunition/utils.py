"""Module to transform ammunition data into new categories"""
from numpy import nan
from pandas import DataFrame, isna
from data.col_names import DefaultColumns
from .consts import ammo_types


def assign_new_ammo_type(ammunition: str) -> str:
    """fit ammunition column data into newly created categories"""
    for ammo_type in ammo_types:
        if ammunition in ammo_type["items"]:
            return ammo_type["type"]

    raise ValueError(f"Unknown ammunition type: {ammo_type}")


def format_ammunition_data(data_frame: DataFrame) -> None:
    """function to format ammunition data into new categories"""
    for row in data_frame.index:
        ammunition = data_frame[DefaultColumns.AMMUNITION][row]
        injury_type = data_frame[DefaultColumns.TYPE_OF_INJURY][row]

        if not isna(ammunition):
            data_frame.at[row, DefaultColumns.AMMUNITION] = assign_new_ammo_type(
                ammunition
            )
        elif injury_type not in ["explosion", "house demolition", nan]:
            data_frame.at[row, DefaultColumns.AMMUNITION] = assign_new_ammo_type(
                injury_type
            )

    data_frame.drop(columns=[DefaultColumns.TYPE_OF_INJURY], inplace=True)
    data_frame.dropna(subset=[DefaultColumns.AMMUNITION], inplace=True)
