from pandas import DataFrame, isna
from data.col_names import Default_columns
from gpt4.prompts import ammunition_assistant_prompt
from gpt4.config import perform_llm_prompt_request
from .consts import ammo_types
from numpy import nan
from transformers.utils import chunkate_notes


# for sorted args which have data
def assign_new_ammo_type(ammunition: str) -> str:
    """fit ammunition column data into newly created categories"""
    for ammo_type in ammo_types:
        if ammunition in ammo_type["items"]:
            return ammo_type["type"]

    print(ammunition, isna(ammunition), ammo_type)
    raise ValueError(f"Unknown ammunition type: {ammo_type}")


def format_ammunition_data(data_frame: DataFrame) -> None:
    for row in data_frame.index:
        ammunition = data_frame[Default_columns.AMMUNITION][row]
        injury_type = data_frame[Default_columns.TYPE_OF_INJURY][row]

        if not isna(ammunition):
            data_frame.at[row, Default_columns.AMMUNITION] = assign_new_ammo_type(
                ammunition
            )
        elif injury_type not in ["explosion", "house demolition", nan]:
            print(ammunition, injury_type, len(injury_type), isna(injury_type))
            data_frame.at[row, Default_columns.AMMUNITION] = assign_new_ammo_type(
                injury_type
            )

    data_frame.drop(columns=[Default_columns.TYPE_OF_INJURY], inplace=True)


def get_missing_ammunition_from_notes(data_frame: DataFrame) -> None:
    missing_values = data_frame[data_frame[Default_columns.AMMUNITION].isna()]
    missing_notes = data_frame[data_frame[Default_columns.NOTES].isna()]
    rows_to_drop = data_frame[missing_values & missing_notes]

    data_frame.drop(rows_to_drop, inplace=True)

    chunks = chunkate_notes(missing_values)

    for chunk in chunks:
        chunk_values = data_frame.loc[chunk, Default_columns.NOTES].tolist()
        prompt = "\n\n".join(chunk_values)

        llm_response = perform_llm_prompt_request(
            assistant_message=ammunition_assistant_prompt,
            user_prompt=prompt,
        )

        for index, value in zip(chunk, llm_response):
            data_frame.at[index, Default_columns.AMMUNITION] = value
