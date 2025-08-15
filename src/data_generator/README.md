# SmartPickr Data Generator

Este módulo permite extraer información de todos los animes de tu lista de MyAnimeList exportada en formato XML, obtener sus datos relevantes usando la API de MAL y guardar los resultados en dos formatos:
- `mock_animes.json`: lista de diccionarios en formato JSON.
- `mock_animes.txt`: script Python en una sola línea, fácil de copiar y pegar.

## Requisitos

- Python 3.8+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Archivos

- `data_generator.py`: script principal.
- `animelist_XXXX.xml`: tu lista exportada desde MyAnimeList (debe estar en la misma carpeta).
- `requirements.txt`: dependencias necesarias.
- `mock_animes.json`: salida con todos los animes en formato JSON.
- `mock_animes.txt`: salida en formato Python copiable.

## Manual de uso

1. Exporta tu lista de animes desde MyAnimeList en formato XML y colócala en esta carpeta.
2. Renombra el archivo XML a `animelist_1755260397_-_10513306.xml` o ajusta el nombre en el script si es necesario.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el script:
   ```bash
   python data_generator.py
   ```
5. Al finalizar, encontrarás los archivos `mock_animes.json` y `mock_animes.txt` en la misma carpeta.

## Notas
- El script siempre guarda y lee archivos en la carpeta donde está ubicado, sin importar desde dónde lo ejecutes.
- La cantidad de temporadas es generada de forma determinista y con una distribución realista.
- Si la API de MAL falla para algún anime, el script reintenta automáticamente.

## Ejemplo de salida en mock_animes.txt

```
mock_animes: list[dict] = [{"id": 1, "title": "Ejemplo", "description": "Descripción de ejemplo.", "seasons": 1, "episodes": 12, "image_url": "https://ejemplo.com/imagen.jpg"}]
return mock_animes
```
