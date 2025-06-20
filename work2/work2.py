from pathlib import Path

path_to_file_cats = Path("cats_file.txt")

def get_cats_info(path):
    cats = []
    if path.exists():
        with open(path, encoding="utf-8") as file_cats:
            lines = [el.strip() for el in file_cats.readlines()]
        for line in lines:
            cat = line.split(',')
            cats.append({"id": cat[0], "name": cat[1], "age": cat[2]})

    else:
        print(f'Файл {path} не існує')
    return cats

cats_info = get_cats_info(path_to_file_cats)
if cats_info:
    print(cats_info)