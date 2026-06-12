import logging

import pandas as pd


def read_data(data_length: int) -> pd.DataFrame:
    df = pd.read_csv("dataset/train.csv", nrows=data_length)
    logging.info(f"Data read completed. Shape: {df.shape}")
    return df
