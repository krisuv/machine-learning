from pandas import DataFrame
from enums import Default_columns


def transform_took_part_in_hostilities(data_frame: DataFrame) -> None:
    data_frame.dropna(columns=[Default_columns.TOOK_PART_IN_THE_HOSTILITIES], inplace=True)
    pass


    