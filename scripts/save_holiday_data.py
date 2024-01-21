import sys
from utils.file_utils import save_to_csv_file
from api.get_islamic_holidays import get_islamic_holidays, get_data_concurrently
from api.get_jewish_holidays import get_jewish_holidays


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
