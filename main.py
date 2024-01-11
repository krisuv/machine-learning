"""main program"""
import sys
from utils.api_utils import get_data_concurrently
from utils.file_utils import save_to_csv_file
from utils.date_utils import get_jewish_holidays, get_islamic_holidays
from data_frame import prepare_data_frame, format_data_frame_categorical_data

# get data about jewish holidays and save in data/jewish.holidays.csv
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

data_frame = prepare_data_frame()
data_frame_transformed = format_data_frame_categorical_data(data_frame)
