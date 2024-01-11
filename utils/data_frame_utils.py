from formatters import format_ammunition
from pandas import DataFrame
from math import nan, isnan
from enums import Default_columns, UNKNOWN_VALUE
from gpt4.prompts import ammunition_assistant_prompt
from gpt4.config import chat_gpt4
from pandas import isna, Series
import ast


def format_ammunition_data(row: Series) -> str:
    if not isna(row[Default_columns.AMMUNITION]):
        return row[Default_columns.AMMUNITION]

    if row[Default_columns.TYPE_OF_INJURY] in ["explosion", "house demolition", nan]:
        return UNKNOWN_VALUE

    return format_ammunition(row[Default_columns.AMMUNITION])


def gpt4_get_ammunition_from_notes(rows: list[Series]) -> list[Series]:
    rows_copy = rows
    notes_list = rows_copy.map(lambda row: row[Default_columns.NOTES])
    notes_list_prompt = ", ".join(notes_list)

    llm_response = chat_gpt4(
        assistant_message=ammunition_assistant_prompt, user_prompt=notes_list_prompt
    )

    ammunition_list = llm_response.split(",")

    rows_copy[Default_columns.AMMUNITION] = ammunition_list

    return rows_copy


def get_missing_ammunition_from_llm(data_frame: DataFrame):
    # Split the 'AMMUNITION' column into chunks of 5
    chunks = [
        data_frame[Default_columns.AMMUNITION][i : i + 5]
        for i in range(0, len(data_frame[Default_columns.AMMUNITION]), 5)
    ]

    processed_chunks = [gpt4_get_ammunition_from_notes(chunk) for chunk in chunks]

    flattened_list = [item for sublist in processed_chunks for item in sublist]
    data_frame[Default_columns.AMMUNITION] = data_frame.Series(flattened_list)

    return data_frame


def format_transform_ammunition_data(data_frame: DataFrame) -> DataFrame:
    data_frame[Default_columns.AMMUNITION] = data_frame[
        Default_columns.AMMUNITION
    ].apply(lambda element: format_ammunition_data(element))

    condition = (data_frame[Default_columns.AMMUNITION] == UNKNOWN_VALUE) & (
        data_frame[Default_columns.NOTES].isna()
    )
    data_frame = data_frame[~condition]

    unknown_indices = data_frame[
        data_frame[Default_columns.AMMUNITION] == UNKNOWN_VALUE
    ].index

    data_frame.loc[unknown_indices, Default_columns.AMMUNITION] = data_frame.loc[
        unknown_indices, Default_columns.AMMUNITION
    ].apply(get_missing_ammunition_from_llm)
