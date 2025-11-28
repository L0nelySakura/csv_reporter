import csv
from pathlib import Path


def read_csv_file(file_path):
    path = Path(file_path)

    try:
        with open(path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            print(list(reader))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    read_csv_file("employees1.csv")
