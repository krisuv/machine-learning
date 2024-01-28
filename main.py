"""main program"""
from data.col_names import TransformedColumns
from data_frame_setup import (
    create_data_frame,
    drop_redundant_columns,
    transform_columns,
    decision_tree_prediction,
)


def main() -> None:
    """main function that runs the program

    create_data_frame() is a function that creates DataFrame instance

    drop_redundant_columns() is a function that drops redundant columns from the DataFrame instance

    transform_columns() is a function that transforms the columns of the DataFrame
    instance from categorical to regression data
    """
    data_frame = create_data_frame()
    drop_redundant_columns(data_frame)
    transform_columns(data_frame)
    decision_tree_prediction(
        data_frame,
        features=[
            TransformedColumns.AGE,
            TransformedColumns.IS_PALESTINIAN,
            TransformedColumns.IS_ISRAELI,
            TransformedColumns.IS_FEMALE,
            TransformedColumns.IS_MALE,
            TransformedColumns.EVENT_LOCATION_GAZA_STRIP,
            TransformedColumns.EVENT_LOCATION_WEST_BANK,
            TransformedColumns.EVENT_LOCATION_ISRAEL,
            TransformedColumns.KILLED_BY_IDF,
            TransformedColumns.KILLED_BY_ISRAELI_CIVILIAN,
            TransformedColumns.KILLED_BY_PALESTINIAN,
            TransformedColumns.DATE_ISLAMIC_HOLIDAY,
            TransformedColumns.DATE_JEWISH_HOLIDAY,
            TransformedColumns.AMMUNITION_FIREARMS,
            TransformedColumns.AMMUNITION_GROUND_EXPLOSIVES,
            # TransformedColumns.AMMUNITION_AIR_EXPLOSIVES,
            TransformedColumns.AMMUNITION_MELEE_WEAPONS,
        ],
        predicator=TransformedColumns.AMMUNITION_AIR_EXPLOSIVES
    )


main()
