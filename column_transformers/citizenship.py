""" Transform 'citizenship' column """
from pandas import DataFrame
from enums import Default_columns, Restructured_columns
from column_transformers.one_hot_encoder import transform_categorical_data


def transform_citizenship(data_frame: DataFrame) -> None:
    """
    remove rows with missing citizenship or other than
    transform column into 'is_israeli' and 'is_palestinian' columns
    """
    # drop rows with missing 'citizenship' values
    data_frame.dropna(subset=[Default_columns.CITIZENSHIP], inplace=True)
    # drop 20 rows where 'citizenship' is neither 'Israeli' or 'Palestinian'
    data_frame.drop(
        data_frame[
            ~data_frame[Default_columns.CITIZENSHIP].isin(["Palestinian", "Israeli"])
        ].index,
        inplace=True,
    )

    transform_categorical_data(
        data_frame,
        column_name=Default_columns.CITIZENSHIP,
        new_column_names={
            "Israeli": Restructured_columns.IS_ISRAELI,
            "Palestinian": Restructured_columns.IS_PALESTINIAN,
        },
    )
