from pandas import read_csv, DataFrame
from data.col_names import Default_columns
from transformers.ammunition.ammunition import transform_ammunition
from transformers.age import transform_age
from transformers.citizenship import transform_citizenship
from transformers.gender import transform_gender
from transformers.date_of_event.date_of_event import transform_date_of_event
from transformers.killed_by import transform_killed_by
from transformers.took_part_in_hostilities import (
    transform_took_part_in_hostilities,
)


def create_data_frame() -> DataFrame:
    data_frame = read_csv(
        "./data/fatalities_isr_pse_conflict_2000_to_2023.csv",
        parse_dates=[Default_columns.DATE_OF_EVENT],
    )

    data_frame[Default_columns.DATE_OF_EVENT] = data_frame[
        Default_columns.DATE_OF_EVENT
    ].dt.strftime("%Y-%m-%d")

    return data_frame


def drop_unwanted_cols(data_frame: DataFrame) -> None:
    # these columns do not contain meaningful data
    # DATE_OF_DEATH can be treated similar to 'date_of_event' as most deceased die in the moment of an event or soon after it. It's also hard to estimate the exact moment of death.
    data_frame.drop(
        columns=[
            Default_columns.NAME,
            Default_columns.DATE_OF_DEATH,
            Default_columns.EVENT_LOCATION,
            Default_columns.EVENT_LOCATION_DISTRICT,
            Default_columns.PLACE_OF_RESIDENCE,
            Default_columns.PLACE_OF_RESIDENCE_DISTRICT,
        ],
        axis=1,
        inplace=True,
    )


def transform_columns(data_frame: DataFrame) -> None:
    transform_date_of_event(data_frame)
    transform_gender(data_frame)
    transform_citizenship(data_frame)
    transform_age(data_frame)
    transform_ammunition(data_frame)
    transform_killed_by(data_frame)
    transform_took_part_in_hostilities(data_frame)
