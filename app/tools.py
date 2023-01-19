from pandas import DataFrame


def data_eng(df: DataFrame) -> DataFrame:
    df = df.drop(columns=["_id", "Time Stamp"])
    df.columns = [col.lower() for col in df.columns]
    return df
