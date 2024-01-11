"""module with functions for getting Jewish and Islamic holidays from 2000 to 2023"""
import math
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from datetime import datetime

START_YEAR = 2000
END_YEAR = 2023


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
    except RequestException as req_err:
        print(f"Request exception occurred: {req_err}")


def get_islamic_holidays(ordinal: int, cpu_threads_amount: int) -> list[dict[str, str]]:
    """Function getting islamic holiday list from external web API https://aladhan.com/islamic-calendar-api."""

    years_total = END_YEAR - START_YEAR

    period_years = math.ceil(years_total / cpu_threads_amount)
    holiday_dates = []

    period_start_year = START_YEAR + (period_years * ordinal)
    period_end_year = period_start_year + period_years

    for year in range(period_start_year, period_end_year):
        for month in range(1, (12 + 1)):
            try:
                print(
                    f"in progress... {month}.{year} (working on thread #{ordinal + 1})"
                )
                url = f"http://api.aladhan.com/v1/gToHCalendar/{month}/{year}"
                response = requests.get(url, timeout=200)
                response.raise_for_status()

                data_list_json = response.json()
                data_list = data_list_json["data"]

                data_filtered = list(
                    filter(lambda day: len(day["hijri"]["holidays"]) > 0, data_list)
                )

                # save only 1st holiday, if more take place the same day
                dates_list = list(
                    map(
                        lambda day: {
                            "date": datetime.strptime(day["gregorian"]["date"], '%Y-%m-%d'),
                            "name": day["hijri"]["holidays"][0],
                        },
                        data_filtered,
                    )
                )

                holiday_dates = holiday_dates + dates_list

            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err}")
            except Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err}")

    return holiday_dates
