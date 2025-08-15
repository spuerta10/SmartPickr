import os
import json

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out/mock_anime_titles.json')

titles = []

for filename in os.listdir(OUT_DIR):
	if filename.endswith('.json'):
		file_path = os.path.join(OUT_DIR, filename)
		with open(file_path, 'r', encoding='utf-8') as f:
			try:
				data = json.load(f)
				# Si el json es una lista de dicts con 'title'
				if isinstance(data, list):
					for item in data:
						if isinstance(item, dict) and 'title' in item:
							titles.append(item['title'])
				# Si el json es un dict con una lista bajo alguna clave
				elif isinstance(data, dict):
					for v in data.values():
						if isinstance(v, list):
							for item in v:
								if isinstance(item, dict) and 'title' in item:
									titles.append(item['title'])
			except Exception as e:
				print(f'Error leyendo {file_path}: {e}')

with open(output_file, 'w', encoding='utf-8') as f:
	json.dump(titles, f, ensure_ascii=False, indent=2)
print(f'Títulos extraídos y guardados en {output_file}')
