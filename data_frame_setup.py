""" This module is responsible for setting up the data frame. """
from pandas import read_csv, DataFrame, set_option, concat
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from data.col_names import DefaultColumns, TransformedColumns
from transformers.ammunition.ammunition import transform_ammunition
from transformers.age import transform_age
from transformers.citizenship import transform_citizenship
from transformers.gender import transform_gender
from transformers.date_of_event.date_of_event import transform_date_of_event
from transformers.killed_by import transform_killed_by
from transformers.event_location_region import transform_event_location_region
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from df_setup.col_relations import exclude_relations


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


def balance_data(data_frame: DataFrame, column_name: TransformedColumns) -> DataFrame:
    """balance the data frame by removing rows with too big representation of certain values"""
    data_frame_0 = data_frame[data_frame[column_name] == 0]
    data_frame_1 = data_frame[data_frame[column_name] == 1]

    min_size = min(len(data_frame_0), len(data_frame_1))

    data_frame_0_balanced = data_frame_0.sample(n=min_size)
    data_frame_1_balanced = data_frame_1.sample(n=min_size)

    data_frame_balanced = concat([data_frame_0_balanced, data_frame_1_balanced])

    data_frame_balanced = shuffle(data_frame_balanced).reset_index(drop=True)

    return data_frame_balanced


def decision_tree_prediction(
    data_frame: DataFrame,
) -> None:
    column_names: list[TransformedColumns] = data_frame.columns.to_list()
    predicator: TransformedColumns = input(
        f"Select column to predict (possible columns: {', '.join(column_names)}):\n"
    )

    if predicator not in column_names:
        raise ValueError("Column name not found in the data frame.")

    features = list(
        filter(
            lambda column_name: column_name != predicator,
            column_names,
        )
    )

    features = exclude_relations(features, predicator)
    
    data_frame = balance_data(data_frame, predicator)

    (X_train, X_test, y_train, y_test) = train_test_split(
        data_frame[features], data_frame[predicator], test_size=0.5
    )

    X_train.columns = X_train.columns.map(str)
    X_test.columns = X_test.columns.map(str)

    decision_tree = DecisionTreeClassifier()

    decision_tree.fit(X_train, y_train)

    predictions = decision_tree.predict(X_test)

    # Evaluation metrics
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Classification Report:\n", classification_report(y_test, predictions))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
