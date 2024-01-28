""" Transform 'citizenship' column """
from pandas import DataFrame
from data.col_names import DefaultColumns, TransformedColumns
from transformers.utils import transform_categorical_data


def transform_citizenship(data_frame: DataFrame) -> None:
    """
    remove rows with missing citizenship or other than
    transform column into 'is_israeli' and 'is_palestinian' columns
    """
    # drop rows with missing 'citizenship' values
    data_frame.dropna(subset=[DefaultColumns.CITIZENSHIP], inplace=True)
    # drop 20 rows where 'citizenship' is neither 'Israeli' or 'Palestinian'
    data_frame.drop(
        data_frame[
            ~data_frame[DefaultColumns.CITIZENSHIP].isin(["Palestinian", "Israeli"])
        ].index,
        inplace=True,
    )

    transform_categorical_data(
        data_frame,
        column_name=DefaultColumns.CITIZENSHIP,
        new_column_names={
            "Israeli": TransformedColumns.IS_ISRAELI,
            "Palestinian": TransformedColumns.IS_PALESTINIAN,
        },
    )
