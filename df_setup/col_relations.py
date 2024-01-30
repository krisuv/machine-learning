""" utilities for column relations:
excluded_relations: list of lists of column names that must not be used together
"""
from data.col_names import TransformedColumns

excluded_relations = [
    [
        TransformedColumns.IS_ISRAELI,
        TransformedColumns.IS_PALESTINIAN,
        TransformedColumns.KILLED_BY_IDF,
        TransformedColumns.KILLED_BY_ISRAELI_CIVILIAN,
        TransformedColumns.KILLED_BY_PALESTINIAN,
    ],
    [TransformedColumns.IS_FEMALE, TransformedColumns.IS_MALE],
    [
        TransformedColumns.AMMUNITION_AIR_EXPLOSIVES,
        TransformedColumns.AMMUNITION_FIREARMS,
        TransformedColumns.AMMUNITION_GROUND_EXPLOSIVES,
        TransformedColumns.AMMUNITION_MELEE_WEAPONS,
        TransformedColumns.AMMUNITION_OTHER,
    ],
    [TransformedColumns.DATE_ISLAMIC_HOLIDAY, TransformedColumns.DATE_JEWISH_HOLIDAY],
    [
        TransformedColumns.EVENT_LOCATION_GAZA_STRIP,
        TransformedColumns.EVENT_LOCATION_ISRAEL,
        TransformedColumns.EVENT_LOCATION_WEST_BANK,
    ],
]


def exclude_relations(column_names: list[str], predicator: str) -> list[str]:
    features = column_names
    for excluded_relation in excluded_relations:
        if predicator in excluded_relation:
            features = list(
                filter(
                    lambda column_name: column_name not in excluded_relation,
                    column_names,
                )
            )
    return features
