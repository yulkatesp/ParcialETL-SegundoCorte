# ***Instrucciones README***

* ***Estructura del proyecto***

        Parcial-BigData/
        ├── Config/
        │   └── config.py
        ├── Extract/
        │   └── extract.py
        ├── Load/
        │   └── load.py
        ├── Transform/
        │   └── transform.py
        ├── notebooks/
        │   ├── 01_etl.ipynb
        │   ├── 02_eda.ipynb
        │   ├── stock_analysis_clean.csv
        │   └── stock_senti_analysis.csv
        ├── main.py
        └── README.md

  * ***Instrucciones de ejecución***

    1. Instalar dependencias necesarias
  
            pip install -r requirements.txt

    2. Ejecutar el pipeline completo

            python main.py

    3. Abrir los notebooks para análisis adicional
       
            notebooks/01_etl.ipynb → ejecución paso a paso del proceso ETL
            notebooks/02_eda.ipynb → análisis exploratorio y visualización de resultados

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> ee52224 (Update)
=======
>>>>>>> 46b4538 (Initial Dockerized Python app)
* ***Explicación del proyecto***
  * **Extract:** Obtiene los datos de origen (archivos CSV o fuentes externas) y los prepara para la transformación.
  * **Transform:** Limpia, normaliza y fusiona los datos. Se manejan valores nulos, se convierten tipos y se calculan métricas relevantes.
  * **Load:** Carga los datos transformados en archivos CSV limpios (stock_analysis_clean.csv y stock_senti_analysis.csv) o bases de datos según la configuración.



* ***Resultados del proyecto***
  * Se logró una limpieza efectiva de los datos con una reducción significativa de valores faltantes.

  *  Se identificaron tendencias positivas entre el sentimiento del mercado y el incremento de precios en ciertos períodos.

  * El análisis permite establecer patrones predictivos preliminares útiles para modelado futuro.
    
* ***Tecnologías utilizadas***

    * Python 3.10+

    * Pandas, NumPy, Matplotlib

    * Jupyter Notebooks

<<<<<<< HEAD
    * Estructura modular ETL (carpetas Extract, Transform, Load)
=======
    * Estructura modular ETL (carpetas Extract, Transform, Load)
>>>>>>> ee52224 (Update)
