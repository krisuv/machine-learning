"""module with functions for getting Islamic holidays from 2000 to 2023"""
import math
from datetime import datetime
import requests
from requests.exceptions import HTTPError, Timeout
from api.constants import START_YEAR, END_YEAR
from concurrent.futures import ThreadPoolExecutor


def get_data_concurrently(function, cpu_threads_amount) -> list:
    with ThreadPoolExecutor(max_workers=cpu_threads_amount) as executor:
        future_to_ordinal = {
            executor.submit(function, ordinal, cpu_threads_amount): ordinal
            for ordinal in range(cpu_threads_amount)
        }

        data = []
        for future in future_to_ordinal:
            data += future.result()

    return data


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
                            "date": datetime.strptime(
                                day["gregorian"]["date"], "%Y-%m-%d"
                            ),
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
