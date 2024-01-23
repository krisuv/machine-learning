from pandas import DataFrame
from data.col_names import Default_columns


# remove 'notes' column from the final DataFrame
def remove_notes(data_frame: DataFrame) -> None:
    return data_frame.drop(columns=[Default_columns.NOTES], axis=1, inplace=True)
