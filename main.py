import argparse
import sys
from csv_reader import read_csv_files
from performance_review import generate_performance_table


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        nargs="+",
        required=True,
    )
    parser.add_argument(
        '--report',
        type=str,
        required=True,
    )
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()
        try:
            file_data = read_csv_files(args.files)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Ошибка при чтении файлов: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Неизвестная ошибка при чтении файлов: {e}")
            sys.exit(1)

        match args.report:
            case "performance":
                performance_table = generate_performance_table(file_data)
                print(performance_table)
            case _:
                print(f"Неизвестный/нереализованный тип отчёта: {args.report}")

    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
