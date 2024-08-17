# Notebook Similarity Checker

## Descripción

**Notebook Similarity Checker** es una herramienta diseñada para comparar notebooks de Jupyter (`.ipynb`) con el fin de detectar similitudes entre ellos. Esta aplicación es ideal para identificar casos de posible copia/fraude, analizando el contenido de los notebooks y generando un reporte en formato CSV que detalla el nivel de similitud entre los archivos.

La herramienta permite ajustar el umbral de similitud y especificar la ruta de salida para los resultados, proporcionando flexibilidad y control sobre el proceso de comparación.

## Requisitos

- Python 3.7 o superior
- Bibliotecas necesarias:
  - `pandas`
  - `json`
  - `difflib`
  - `argparse`
  - `logging`

Puedes instalar las dependencias necesarias con:
pip install pandas


## Instalación

1. Clona este repositorio o descarga los archivos `main.py` y `similarity_checker.py` en tu máquina local.

2. Asegúrate de tener Python 3.7 o superior instalado.

3. Navega al directorio donde se encuentran los archivos.

## Uso

### Ejecución Básica

Para ejecutar la aplicación, utiliza el siguiente comando en la terminal:

python main.py /ruta/a/tu/carpeta --output /ruta/a/guardar/resultados.csv --threshold 0.8


### Parámetros

- **`folder_path`** (obligatorio): Ruta a la carpeta que contiene los archivos de notebooks Jupyter (`.ipynb`).
- **`--output`** (opcional): Ruta y nombre del archivo CSV donde se guardarán los resultados. Por defecto, se guarda como `similarity_results.csv` en el directorio actual.
- **`--threshold`** (opcional): Nivel de similitud que quieres considerar. El rango es de `0` (sin similitud) a `1` (idénticos). El valor por defecto es `0.9`.

### Ejemplo

python main.py /home/user/notebooks --output /home/user/similarity_results.csv --threshold 0.85


Este comando analizará los notebooks en la carpeta `/home/user/notebooks`, generará un reporte de similitud con un umbral del 85%, y guardará los resultados en `/home/user/similarity_results.csv`.

## Manejo de Errores

La herramienta está diseñada para manejar errores comunes, como:

- Carpetas no existentes o vacías.
- Problemas de lectura de archivos.
- Errores durante la comparación de similitud o la generación del archivo CSV.

En caso de que ocurra un error, este será registrado en la terminal, permitiendo que el proceso continúe siempre que sea posible.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, siéntete libre de abrir un Pull Request o reportar un Issue.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
