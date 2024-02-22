import pandas as pd


class IngestData:
    def __init__(self) -> None:
        self.data_path = None

    def get_data(self, path: str) -> pd.DataFrame:
        self.data_path = path
        df = pd.read_csv(self.data_path, encoding = "ISO-8859-1")
        return df