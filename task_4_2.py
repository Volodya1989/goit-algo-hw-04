from pathlib import Path


def get_cats_info(path: str) -> list[dict]:
    path = Path(path).resolve()

    if not path.exists():
        print(
            f"Path to the file '{path}' is incorrect or file does not exists.")
        return []

    cats_info = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                id_, name, age = line.strip().split(',')
                cats_info.append({"id": id_, "name": name, "age": age})
            except ValueError:
                print(
                    f"Error: Invalid line: {line.strip()}")

    return cats_info


print(get_cats_info("./cats.txt"))
