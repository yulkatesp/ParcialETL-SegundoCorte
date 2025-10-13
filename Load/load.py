class Loader:

    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path):
        try:
            self.df.to_csv(output_path, index = False)
            print(f" - Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")