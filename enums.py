from enum import Enum

UNKNOWN_VALUE = 'unknown'

class Citizenship(str, Enum):
    """Enum meaning person citizenship"""

    ISRAELI = "Israeli"
    PALESTINIAN = "Palestinian"

    def __str__(self) -> str:
        return str.__str__(self)


class Default_columns(str, Enum):
    """Enum with column names in original database"""

    NAME = "name"
    DATE_OF_EVENT = "date_of_event"
    AGE = "age"
    CITIZENSHIP = "citizenship"
    EVENT_LOCATION = "event_location"
    EVENT_LOCATION_DISTRICT = "event_location_district"
    EVENT_LOCATION_REGION = "event_location_region"
    DATE_OF_DEATH = "date_of_death"
    GENDER = "gender"
    TOOK_PART_IN_THE_HOSTILITIES = "took_part_in_the_hostilities"
    PLACE_OF_RESIDENCE = "place_of_residence"
    PLACE_OF_RESIDENCE_DISTRICT = "place_of_residence_district"
    TYPE_OF_INJURY = "type_of_injury"
    AMMUNITION = "ammunition"
    KILLED_BY = "killed_by"
    NOTES = "notes"

    def __str__(self) -> str:
        return str.__str__(self)


class Restructured_columns(str, Enum):
    AGE = "age"
    EVENT_DATE_JEWISH_HOLIDAY = "event_date_jewish_holiday"
    EVENT_DATE_MUSLIM_HOLIDAY = "event_date_muslim_holiday"

    CITIZENSHIP_ISRAELI = "citizenship_israeli"
    CITIZENSHIP_PALESTINIAN = "citizenship_palestinian"

    EVENT_LOCATION_GAZA_STRIP = "event_location_gaza_strip"
    EVENT_LOCATION_WEST_BANK = "event_location_west_bank"
    EVENT_LOCATION_ISRAEL = "event_location_israel"

    SEX_M = "sex_m"
    SEX_F = "sex_f"

    AMMUNITION_FIREARMS = "ammunition_firearms"
    AMMUNITION_GROUND_EXPLOSIVES = "ammunition_ground_explosives"
    AMMUNITION_AIR_EXPLOSIVES = "ammunition_air_explosives"
    AMMUNITION_MELEE_WEAPONS = "ammunition_melee_weapons"
    AMMUNITION_OTHER = "ammunition_other"

    TOOK_PART_IN_HOSTILITIES = "took_part_in_the_hostilities"  # NO - 0, RATHER NO- 0.25 UNKNOWN - 0.5, ('Object of targeted killing') POSSIBLY - 0.75 YES - 1

    KILLED_BY_IDF = "killed_by_idf"
    KILLED_BY_PALESTINIAN = "killed_by_palestinian"
    KILLED_BY_ISRAELI_CIVILIAN = "killed_by_israeli_civilian"

    def __str__(self) -> str:
        return str.__str__(self)
