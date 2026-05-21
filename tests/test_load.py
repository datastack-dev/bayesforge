from bayesforge.data.load import get_data


def test_get_data_returns_dataframe() -> None:
    data = get_data("AAPL", "w")

    assert not data.empty
