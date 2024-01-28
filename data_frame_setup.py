""" This module is responsible for setting up the data frame. """
from pandas import read_csv, DataFrame, set_option
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from data.col_names import DefaultColumns, TransformedColumns
from transformers.ammunition.ammunition import transform_ammunition
from transformers.age import transform_age
from transformers.citizenship import transform_citizenship
from transformers.gender import transform_gender
from transformers.date_of_event.date_of_event import transform_date_of_event
from transformers.killed_by import transform_killed_by
from transformers.event_location_region import transform_event_location_region


def create_data_frame() -> DataFrame:
    """
    create data frame from csv file
    source file access: December 2023
    """
    data_frame = read_csv(
        "./data/fatalities_isr_pse_conflict_2000_to_2023.csv",
        parse_dates=[DefaultColumns.DATE_OF_EVENT],
    )

    set_option("display.max_columns", None)

    return data_frame


def drop_redundant_columns(data_frame: DataFrame) -> None:
    """remove redundant columns from the data frame

    'name' REASON: does not provide any useful information,

    'date_of_death' REASON: date_of_event is used instead,

    'event_location' REASON: too many unique values,

    'event_location_district' REASON: too many unique values,

    'place_of_residence' REASON: too many unique values,

    'place_of_residence_district' REASON: too many unique values,

    'took_part_in_the_hostilities' REASON: too many missing values,
    using LLM API would be too expensive or inefficient for now (might be added in the future)'
    """
    data_frame.drop(
        columns=[
            DefaultColumns.NAME,
            DefaultColumns.DATE_OF_DEATH,
            DefaultColumns.EVENT_LOCATION,
            DefaultColumns.EVENT_LOCATION_DISTRICT,
            DefaultColumns.PLACE_OF_RESIDENCE,
            DefaultColumns.PLACE_OF_RESIDENCE_DISTRICT,
            DefaultColumns.TOOK_PART_IN_THE_HOSTILITIES,
            DefaultColumns.NOTES,
        ],
        axis=1,
        inplace=True,
    )


def transform_columns(data_frame: DataFrame) -> None:
    """function calling all transformers in order for all columns that
    need to be transformed from categorical to regression data"""
    transform_date_of_event(data_frame)
    transform_gender(data_frame)
    transform_citizenship(data_frame)
    transform_age(data_frame)
    transform_killed_by(data_frame)
    transform_event_location_region(data_frame)
    transform_ammunition(data_frame)


def decision_tree_prediction(
    data_frame: DataFrame,
    features: list[TransformedColumns],
    predicator: TransformedColumns,
) -> None:

    (X_train, X_test, y_train, y_test) = train_test_split(
        data_frame[features], data_frame[predicator], test_size=0.5
    )

    X_train.columns = X_train.columns.map(str)
    X_test.columns = X_test.columns.map(str)

    decision_tree = DecisionTreeRegressor()

    decision_tree.fit(X_train, y_train)

    result = decision_tree.predict(X_test)
    mae = mean_absolute_error(y_test, result)
    print("Mean Absolute Error:", mae)