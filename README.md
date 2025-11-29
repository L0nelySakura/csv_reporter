# CSV Reporter

Скрипт для анализа эффективности работы разработчиков на основе данных из CSV-файлов. Обрабатывает информацию о закрытых задачах и формирует отчеты о производительности по позициям.

## Технологии

- [Python](https://www.python.org/) (стандартная библиотека: argparse, csv)
- [tabulate](https://github.com/astanin/python-tabulate) - для вывод таблиц в консоль
- [pytest](https://docs.pytest.org/) - для тестирования кода

## Использование

### Требования

Установите зависимости, указанные [выше](#Технологии)

### Установка и запуск

1) Скачайте репозиторий:
```sh
git clone [<url_репозитория>](https://github.com/L0nelySakura/csv_reporter)
```

2) Перейдите в папку проекта:
```sh
cd csv_reporter
```

3) Установите зависимости:
```sh
pip install -r requirements.txt
```

4) Запуск скрипта:
```sh
python main.py --files <файл1.csv> [файл2.csv ...] --report <название_отчета>
```

### Примеры запуска

Формирование отчета performance по одному файлу:
```sh
python main.py --files employees1.csv --report performance
```

Формирование отчета performance по нескольким файлам:
```sh
python main.py --files employees1.csv employees2.csv --report performance
```

Пример вывода:
```
position               performance
-------------------  -------------
Backend Developer             4.83
DevOps Engineer               4.80
Data Engineer                 4.70
Frontend Developer            4.65
QA Engineer                   4.50
```

## Доступные отчеты

- **performance** - отчет по средней эффективности по позициям. Показывает среднее арифметическое значения performance для каждой позиции, отсортированное по убыванию эффективности.

## Запуск тестов

Запуск всех тестов:
```sh
pytest tests/
```

Запуск тестов с покрытием кода:
```sh
pytest tests/ --cov=. --cov-report=term-missing
```

Запуск тестов с подробным выводом:
```sh
pytest tests/ -v
```

## Формат входных данных

CSV файлы должны содержать следующие колонки:
- `name` - имя сотрудника
- `position` - должность
- `completed_tasks` - количество выполненных задач
- `performance` - оценка эффективности (число)
- `skills` - навыки
- `team` - команда
- `experience_years` - опыт работы в годах

Пример:
```csv
name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django, PostgreSQL, Docker",API Team,5
Maria Petrova,Frontend Developer,38,4.7,"React, TypeScript, Redux, CSS",Web Team,4
```
также примерами служат два .csv файла в директории
