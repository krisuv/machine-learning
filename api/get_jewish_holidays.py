"""module with functions for getting Jewish holidays from 2000 to 2023"""
import requests
from requests.exceptions import HTTPError, Timeout
from api.constants import START_YEAR, END_YEAR


def get_jewish_holidays() -> list[dict[str, str]]:
    """Function getting jewish_holiday list from external web API www.hebcal.com/hebcal."""
    try:
        url = f"https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&mod=on&start={START_YEAR}-01-01&end={END_YEAR}-12-31"
        response = requests.get(url, timeout=50)
        response.raise_for_status()

        data_list_json = response.json()

        data_list = data_list_json["items"]

        holiday_dates = list(
            map(
                lambda holiday: {"date": holiday["date"], "name": holiday["title"]},
                data_list,
            )
        )

        return holiday_dates

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
