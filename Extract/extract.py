import pandas as pd

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        try:
            df = pd.read_csv(self.file_path, encoding='latin1')
            return df

        except Exception as e:
            print(f"Error al extraer los datos {e}")
            return None