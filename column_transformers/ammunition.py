from math import nan
from pandas import DataFrame, isna
from enums import Default_columns, Restructured_columns
from gpt4.prompts import ammunition_assistant_prompt
from gpt4.config import chat_gpt4
from column_transformers import ammo_consts
from column_transformers.one_hot_encoder import transform_categorical_data


# for sorted args which have data
def assign_new_ammo_type(ammunition: str) -> str:
    """fit ammunition column data into newly created categories"""
    for ammo_type in ammo_consts.ammo_types:
        if ammunition in ammo_type["items"]:
            return ammo_type["type"]

    print(ammunition, isna(ammunition), ammo_type)
    raise ValueError(f"Unknown ammunition type: {ammo_type}")


def format_ammunition_data(data_frame: DataFrame) -> None:
    for row in data_frame.index:
        ammunition = data_frame[Default_columns.AMMUNITION][row]
        injury_type = data_frame[Default_columns.TYPE_OF_INJURY][row]
        note = data_frame[Default_columns.NOTES][row]

        # print(ammunition)
        if not isna(ammunition):
            # print(ammunition)
            data_frame.at[row, Default_columns.AMMUNITION] = assign_new_ammo_type(
                ammunition
            )
        elif injury_type not in [
            "explosion",
            "house demolition",
        ] or not isna(injury_type):
            print(injury_type, isna(injury_type))
            data_frame.at[row, Default_columns.AMMUNITION] = assign_new_ammo_type(
                injury_type
            )
        elif isna(note):
            data_frame.drop(row, inplace=True)

    data_frame.drop(columns=[Default_columns.TYPE_OF_INJURY], inplace=True)


def get_missing_ammunition_from_notes(data_frame: DataFrame) -> None:
    nan_values = data_frame[
        data_frame[Default_columns.AMMUNITION].isna()
    ].index.tolist()

    # Split the 'AMMUNITION' column into chunks of 5
    chunks = [nan_values[i : i + 5] for i in range(0, len(nan_values), 5)]

    for chunk in chunks:
        chunk_values = data_frame.loc[chunk, Default_columns.NOTES].tolist()
        notes_list = ", ".join(chunk_values)
        # llm_response = chat_gpt4(
        #     assistant_message=ammunition_assistant_prompt, user_prompt=notes_list
        # )
        llm_response = "[]"
        ammunition_list = llm_response.split(",")

        for index, value in zip(chunk, ammunition_list):
            data_frame.at[index, Default_columns.AMMUNITION] = value


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
