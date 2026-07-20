import pandas as pd

def merge_data(df1, df2):
    """
    Example demonstrating explicit merge parameters.
    """
    return df1.merge(
        df2,
        how="inner",
        on="id"
    )
