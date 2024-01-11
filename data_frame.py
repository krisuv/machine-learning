from pandas import read_csv, DataFrame
import pandas
from enums import Default_columns, Citizenship
from sklearn.preprocessing import LabelEncoder


def prepare_data_frame() -> DataFrame:
    data_frame = read_csv(
        "./data/fatalities_isr_pse_conflict_2000_to_2023.csv",
        parse_dates=[Default_columns.DATE_OF_EVENT],
    )

    # these columns do not contain meaningful data
    # DATE_OF_DEATH can be treated similar to 'date_of_event' as most deceased die in the moment of an event or soon after it. It's also hard to estimate the exact moment of death.
    data_frame = data_frame.drop(
        columns=[
            Default_columns.NAME,
            Default_columns.DATE_OF_DEATH,
            Default_columns.EVENT_LOCATION,
            Default_columns.EVENT_LOCATION_DISTRICT,
            Default_columns.PLACE_OF_RESIDENCE,
            Default_columns.PLACE_OF_RESIDENCE_DISTRICT,
        ]
    )

    # skip 3% of data without age
    data_frame = data_frame.dropna(subset=[Default_columns.AGE])

    # skip deaths of people not being Israeli or Palestinian
    foreigners = ~data_frame[Default_columns.CITIZENSHIP].isin(
        [Citizenship.ISRAELI, Citizenship.PALESTINIAN]
    )
    data_frame = data_frame.drop(data_frame[foreigners].index)

    # remove rows with no data in 'ammunition' and 'took_part_in_the_hostilities' columns if there aren't 'notes' to fill the missing information
    no_data = (
        data_frame[Default_columns.AMMUNITION].isnull()
        | data_frame[Default_columns.TOOK_PART_IN_THE_HOSTILITIES].isnull()
    ) & data_frame[Default_columns.NOTES].isnull()
    data_frame = data_frame.drop(data_frame[no_data].index)

    # Assuming data_frame is your DataFrame
    missing_both = data_frame[
        data_frame["ammunition"].isnull() & data_frame["type_of_injury"].isnull()
    ]
    count_missing_both = len(missing_both)
    print(
        "Number of rows missing both ammunition and type_of_injury:", count_missing_both
    )

    missing_ammunition_has_injury = data_frame[
        data_frame["ammunition"].isnull() & data_frame["type_of_injury"].notnull()
    ]
    count_missing_ammunition_has_injury = len(missing_ammunition_has_injury)
    print(
        "Number of rows missing ammunition but have type_of_injury:",
        count_missing_ammunition_has_injury,
    )

    return data_frame


def format_data_frame_categorical_data(data_frame: DataFrame) -> DataFrame:
    data_frame_transformed = data_frame

    # transform gender
    label_encoder = LabelEncoder()
    data_frame_transformed[Default_columns.GENDER] = label_encoder.fit_transform(
        data_frame_transformed[Default_columns.GENDER]
    )
    print(data_frame_transformed)
    print(data_frame_transformed[Default_columns.GENDER].unique())

    # one_hot_encoder = OneHotEncoder(handle_unknown='ignore')
    # one_hot_encoder.categories_[array([Citizenship.PALESTINIAN, Citizenship.ISRAELI], dtype=object), array([1, 2, 3], dtype=object)]
    data_frame_enc = pandas.get_dummies(
        data_frame[Default_columns.CITIZENSHIP],
        prefix=Default_columns.CITIZENSHIP,
        dtype=float,
    )
    print(data_frame_enc.head())

    return data_frame_transformed
