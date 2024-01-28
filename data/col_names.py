""" Enums for initial column names and column names after transformations """
from enum import Enum


class DefaultColumns(str, Enum):
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


class TransformedColumns(str, Enum):
    """Enum with new column names after transformations"""
    AGE = "age"

    DATE_JEWISH_HOLIDAY = "date_jewish_holiday"
    DATE_ISLAMIC_HOLIDAY = "date_islamic_holiday"

    IS_ISRAELI = "is_israeli"
    IS_PALESTINIAN = "is_palestinian"

    EVENT_LOCATION_GAZA_STRIP = "event_location_gaza_strip"
    EVENT_LOCATION_WEST_BANK = "event_location_west_bank"
    EVENT_LOCATION_ISRAEL = "event_location_israel"

    IS_MALE = "is_male"
    IS_FEMALE = "is_female"

    AMMUNITION_FIREARMS = "ammunition_firearms"
    AMMUNITION_GROUND_EXPLOSIVES = "ammunition_ground_explosives"
    AMMUNITION_AIR_EXPLOSIVES = "ammunition_air_explosives"
    AMMUNITION_MELEE_WEAPONS = "ammunition_melee_weapons"
    AMMUNITION_OTHER = "ammunition_other"

    KILLED_BY_IDF = "killed_by_idf"
    KILLED_BY_PALESTINIAN = "killed_by_palestinian"
    KILLED_BY_ISRAELI_CIVILIAN = "killed_by_israeli_civilian"

    def __str__(self) -> str:
        return str.__str__(self)
