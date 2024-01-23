from pandas import DataFrame
from data.col_names import Default_columns
from gpt4.config import perform_llm_prompt_request
from gpt4.prompts import took_part_in_hostilities_prompt
from transformers.utils import chunkate_notes

def transform_took_part_in_hostilities(data_frame: DataFrame) -> None:
    missing_values = data_frame[
        data_frame[Default_columns.TOOK_PART_IN_THE_HOSTILITIES].isna()
    ]
    missing_notes = data_frame[data_frame[Default_columns.NOTES].isna()]
    rows_to_drop = data_frame[missing_values & missing_notes]

    # drop rows where value 'took_part_in_the_hostilities' and 'notes' are both empty
    data_frame.drop(rows_to_drop, inplace=True)

    chunks = chunkate_notes(missing_values)

    for chunk in chunks:
        chunk_values = data_frame.loc[chunk, Default_columns.NOTES].tolist()
        prompt = "\n\n".join(chunk_values)

        llm_response = perform_llm_prompt_request(
            assistant_message=took_part_in_hostilities_prompt,
            user_prompt=prompt,
        )

        for index, value in zip(chunk, llm_response):
            data_frame.at[index, Default_columns.AMMUNITION] = value
