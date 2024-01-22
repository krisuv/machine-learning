from pandas import DataFrame, concat, get_dummies


def chunkate_notes(missing_values: DataFrame, chunk_size: int = 5) -> list:
    nan_values = missing_values.index.tolist()
    return [
        nan_values[i : i + chunk_size] for i in range(0, len(nan_values), chunk_size)
    ]


def transform_categorical_data(
    data_frame: DataFrame, column_name: str, new_column_names: dict[str, str]
) -> None:
    one_hot = get_dummies(
        data_frame,
        columns=[column_name],
        prefix="",
        prefix_sep="",
    )

    one_hot.rename(
        columns=new_column_names,
        inplace=True,
    )

    data_frame.drop(columns=[column_name], axis=1, inplace=True)

    data_frame = concat([data_frame, one_hot], axis=1)
