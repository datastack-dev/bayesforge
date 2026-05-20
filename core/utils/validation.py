from utils.data_load import load_single_asset,load_multiple_assets


def clean_data(data):
    data=data.dropna()
    return data
