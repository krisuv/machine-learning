from pandas import DataFrame
import pandas
from sklearn import preprocessing

# from enums import Default_columns


def transform_gender(data_frame: DataFrame):
    label_encoder = preprocessing.LabelEncoder()

    print(data_frame["gender"].unique())

    data_frame = data_frame.dropna(subset=["gender"])

    data_frame["gender"] = label_encoder.fit_transform(data_frame["gender"])

    print(data_frame["gender"].unique())


data_frame = pandas.read_csv("data/fatalities_isr_pse_conflict_2000_to_2023.csv")


transform_gender(data_frame)
print(data_frame['gender'].head())
