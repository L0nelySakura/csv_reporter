import csv
from pathlib import Path


def read_csv_file(file_path: str) -> list[dict[str, str]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    if not path.is_file():
        raise FileNotFoundError(f"Путь не является файлом: {file_path}")

    try:
        with open(path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            employees = list(reader)
    except Exception as e:
        raise Exception(f"Ошибка при обработке .csv файла: {e}")
    return employees


def read_csv_files(file_paths: list[str]) -> list[dict[str, str]]:
    all_employees = []
    for file_path in file_paths:
        employees = read_csv_file(file_path)
        all_employees.extend(employees)
    return all_employees


if __name__ == "__main__":
    print(read_csv_file("employees1.csv"))
    print(read_csv_file("employees2.csv"))
    print(read_csv_files(["employees1.csv", "employees2.csv"]))
