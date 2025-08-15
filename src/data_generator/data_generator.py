import mal  # pip install mal-api
import mal.config
import json
from xml.dom.minidom import parse
from time import sleep
import hashlib
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
XML_PATH = os.path.join(SCRIPT_DIR, "animelist_1755260397_-_10513306.xml")

DELAY = 2.5
mal.config.TIMEOUT = 30


def get_all_anime_ids_titles(xml_path):
    DOMTree = parse(xml_path)
    collection = DOMTree.documentElement
    media_list_xml = collection.getElementsByTagName("anime")
    animes = []
    for media in media_list_xml:
        anime_id = media.getElementsByTagName("series_animedb_id")[0].childNodes[0].data
        title = media.getElementsByTagName("series_title")[0].childNodes[0].data
        animes.append({"id": int(anime_id), "title": title})
    return animes


def deterministic_seasons(title):
    # Hash estable
    h = hashlib.md5(title.encode()).hexdigest()
    # Convertimos los primeros 8 caracteres a int
    num = int(h[:8], 16)
    # Normalizamos a [0,1]
    x = num / 0xFFFFFFFF
    # Distribución inversa: 1 temp muy probable, 4-5 muy raro
    # Usamos una función tipo exponencial inversa
    # p = 1 - exp(-3x) para sesgar hacia 1
    # Definimos los rangos
    if x < 0.7:
        return 1
    elif x < 0.88:
        return 2
    elif x < 0.97:
        return 3
    elif x < 0.995:
        return 4
    else:
        return 5


def get_anime_info(anime_id):
    try:
        anime = mal.Anime(anime_id)
        seasons = deterministic_seasons(anime.title)
        return {
            "id": anime.mal_id,
            "title": anime.title,
            "description": anime.synopsis or "",
            "seasons": seasons,
            "episodes": anime.episodes or 0,
            "image_url": anime.image_url or "",
        }
    except Exception as e:
        print(
            f"\tError obteniendo anime {anime_id}: {e}. (Seguramente nos rate-limitearon)"
        )
        return None


def main():
    print("Extrayendo IDs y títulos del XML...")
    anime_list = get_all_anime_ids_titles(XML_PATH)
    print(f"Total animes encontrados: {len(anime_list)}")
    mock_animes = []
    for i, anime in enumerate(anime_list, 1):
        n_try = 0
        while True:
            info = get_anime_info(anime["id"])
            if info:
                mock_animes.append(info)
                break
            else:
                delay = DELAY + n_try * 10
                print(f"\tTry #{n_try+2}, delaying {delay} seconds...")
                sleep(delay)
                n_try += 1
        print(f'[{i}/{len(anime_list)}] {anime["title"]} procesado')
        sleep(DELAY)
    # Guardar en JSON
    json_path = os.path.join(SCRIPT_DIR, "mock_animes.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(mock_animes, f, ensure_ascii=False, indent=4)
    print(f"Datos guardados en {json_path}")

    # Guardar en TXT en una sola línea estilo Python
    txt_content = f"mock_animes: list[dict] = {json.dumps(mock_animes, ensure_ascii=False)}\nreturn mock_animes"
    txt_path = os.path.join(SCRIPT_DIR, "mock_animes.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(txt_content)
    print(f"Datos guardados en {txt_path} (formato copiable)")
    return mock_animes


if __name__ == "__main__":
    mock_animes = main()
