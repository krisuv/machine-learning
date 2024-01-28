""" This script is used to import islamic holidays from the API and save them to a csv file. """
import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from api.get_islamic_holidays import get_islamic_holidays, get_data_concurrently
from scripts.utils import save_to_csv_file

islamic_holiday_dates = get_data_concurrently(
    function=get_islamic_holidays, cpu_threads_amount=int(sys.argv[1])
)
save_to_csv_file(file_name="islamic_holidays", data=islamic_holiday_dates)
