import numpy as np
import pandas as pd

from bayesforge.data.load import get_data


def get_daily_return(
    ticker: str,
    horizon: str,
    lookback: int,
) -> pd.Series:
    """
    Extract the daily return of the ticker symbol
    according to the horizon and lookback provided
    by the user.
    """

    df = get_data(ticker, horizon, lookback)
    close = df["Close"]

    returns = close.pct_change()

    return returns


def get_log_returns(
    ticker: str,
    horizon: str,
    lookback: int,
) -> pd.Series:
    """
    Convert returns to log returns.
    """

    df = get_data(ticker, horizon, lookback)

    log_return = np.log(df["Close"] / df["Close"].shift(1))

    return pd.Series(log_return).dropna()
