from Config.config import config
from Extract.extract import Extractor
from Load.load import Loader
from Transform.transform import Transformer


def main():
    print("=== Iniciando proceso ETL ===")

    #EXTRACCIÓN
    extractor = Extractor(config.input_path)
    df = extractor.extract()

    if df is None:
        print("No se pudieron extraer los datos. Proceso detenido.")
        return
    print("✅ Datos extraídos correctamente.")

    #TRANSFORMACIÓN
    transformer = Transformer(df)
    df_clean = transformer.clean()
    print("✅ Datos transformados correctamente.")

    #CARGA
    loader = Loader(df_clean)
    loader.to_csv(config.output_path)
    print("✅ Datos cargados correctamente.")

    print("=== Proceso ETL finalizado con éxito ===")

if __name__ == "__main__":
    main()