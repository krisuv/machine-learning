""" This script imports the Jewish holidays from hebcal.com and saves them to a csv file."""
import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from api.get_jewish_holidays import get_jewish_holidays
from scripts.utils import save_to_csv_file


jewish_holiday_dates = get_jewish_holidays()
save_to_csv_file(file_name="jewish_holidays", data=jewish_holiday_dates)
