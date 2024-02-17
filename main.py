"""main program"""
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
    )


main()
