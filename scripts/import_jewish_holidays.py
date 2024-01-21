from utils.file_utils import save_to_csv_file
from api.get_jewish_holidays import get_jewish_holidays


jewish_holiday_dates = get_jewish_holidays()
save_to_csv_file(
    file_name="jewish_holidays", data=jewish_holiday_dates, fieldnames=["date", "name"]
)
