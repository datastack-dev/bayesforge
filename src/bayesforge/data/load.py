from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

from bayesforge.data.pre_process import preprocess_data

INTERVALS = {
    "d": "5m",
    "w": "1h",
    "m": "1d",
    "a": "1d",
    "y": "1d",
}

LOOKBACKS = {
    "d": 50,
    "w": 365 * 2,
    "m": 365 * 5,
    "a": 365 * 15,
    "y": 365 * 15,
}


def get_data(
    ticker: str,
    horizon: str,
    lookback: int | None = None,
) -> pd.DataFrame:
    """
    Retrieve and preprocess OHLCV market data for a given ticker,
    investment horizon, and optional lookback period. Returns a
    timestamp-indexed pandas DataFrame containing cleaned market data.
    """
    horizon = horizon.lower()

    if horizon not in INTERVALS:
        raise ValueError(f"Invalid horizon: {horizon}")

    interval = INTERVALS[horizon]

    if lookback is None:
        lookback = LOOKBACKS[horizon]

    end_date = datetime.today()
    start_date = end_date - timedelta(days=lookback)

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        interval=interval,
        progress=False,
    )

    return preprocess_data(data)
