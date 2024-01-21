import pandas


def transform_categorical_data(
    data_frame: pandas.DataFrame, column_name: str, new_column_names: dict[str, str]
) -> None:
    one_hot = pandas.get_dummies(
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

    data_frame = pandas.concat([data_frame, one_hot], axis=1)
