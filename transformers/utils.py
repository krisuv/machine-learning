"""Utility functions for the transformers module."""
from pandas import DataFrame, get_dummies


def chunkate_notes(missing_values: DataFrame, chunk_size: int = 5) -> list:
    """Split notes in rows with missing values into chunks of size chunk_size,
    which will be sent to the LMM API for completion of missing value."""
    nan_values = missing_values.index.tolist()
    return [
        nan_values[i : i + chunk_size] for i in range(0, len(nan_values), chunk_size)
    ]


def transform_categorical_data(
    data_frame: DataFrame, column_name: str, new_column_names: dict[str, str]
) -> None:
    """Transform categorical data into one hot encoding columns."""
    one_hot = get_dummies(
        data_frame, columns=[column_name], prefix="", prefix_sep="", dtype="int"
    )

    if not isinstance(new_column_names, dict):
        raise TypeError("new_column_names must be a dictionary")

    one_hot.rename(
        columns=new_column_names,
        inplace=True,
    )

    data_frame.drop(columns=[column_name], axis=1, inplace=True)

    data_frame[one_hot.columns] = one_hot
