"""main program"""
from data_frame import create_data_frame, drop_unwanted_cols, transform_columns

data_frame = create_data_frame()
drop_unwanted_cols(data_frame)
transform_columns(data_frame)
