import numpy as np
import pandas as pd


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess market data by sorting timestamps, removing duplicate
    entries, and imputing missing numeric values using the average
    of the nearest available observations above and below.
    """
    data = data.copy()

    data.sort_index(inplace=True)

    data.drop_duplicates(inplace=True)

    numeric_columns = data.select_dtypes(include=[np.number]).columns

    for column in numeric_columns:
        series = data[column]

        for idx in series[series.isna()].index:
            lower = series.loc[:idx].dropna()
            upper = series.loc[idx:].dropna()

            lower_value = lower.iloc[-1] if not lower.empty else None
            upper_value = upper.iloc[0] if not upper.empty else None

            if lower_value is not None and upper_value is not None:
                data.at[idx, column] = (lower_value + upper_value) / 2

            elif lower_value is not None:
                data.at[idx, column] = lower_value

            elif upper_value is not None:
                data.at[idx, column] = upper_value

    return data
