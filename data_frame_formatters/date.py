from pandas import DataFrame, read_csv
from enums import Default_columns, Restructured_columns
from utils.api_utils import get_data_concurrently
from utils.date_utils import get_islamic_holidays, get_jewish_holidays
from utils.file_utils import save_to_csv_file
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
import sys

jewish_holiday_dates = get_jewish_holidays()
save_to_csv_file(
    file_name="jewish_holidays", data=jewish_holiday_dates, fieldnames=["date", "name"]
)

# get data about jewish holidays and save in data/jewish.holidays.csv
islamic_holiday_dates = get_data_concurrently(
    function=get_islamic_holidays, cpu_threads_amount=int(sys.argv[1])
)
save_to_csv_file(
    file_name="islamic_holidays",
    data=islamic_holiday_dates,
    fieldnames=["date", "name"],
)


def transform_date_of_event(data_frame: DataFrame):
    islamic_holidays = read_csv("data/islamic_holidays.csv", parse_dates=["date"])
    jewish_holidays = read_csv("data/jewish_holidays.csv", parse_dates=["date"])

    islamic_holiday_dates = set(islamic_holidays["date"].dt.date)

    data_frame[Restructured_columns.EVENT_DATE_MUSLIM_HOLIDAY] = data_frame[
        Default_columns.DATE_OF_EVENT
    ].dt.date.apply(lambda x: 1 if x in islamic_holiday_dates else 0)

    jewish_holiday_dates = set(jewish_holidays["date"].dt.date)

    data_frame[Restructured_columns.EVENT_DATE_JEWISH_HOLIDAY] = data_frame[
        Default_columns.DATE_OF_EVENT
    ].dt.date.apply(lambda x: 1 if x in jewish_holiday_dates else 0)

    data_frame = data_frame.drop(Default_columns.DATE_OF_EVENT, axis=1)
