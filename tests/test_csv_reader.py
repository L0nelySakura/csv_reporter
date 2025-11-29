import pytest
import tempfile
import os
from pathlib import Path
from csv_reader import read_csv_file, read_csv_files


class TestReadCsvFile:
    """Тесты для функции read_csv_file"""

    def test_read_valid_csv_file(self):
        """Тест чтения валидного CSV файла"""
        # Создаем временный CSV файл
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f.write('John Doe,Backend Developer,45,4.8,"Python, Django",API Team,5\n')
            temp_path = f.name

        try:
            result = read_csv_file(temp_path)
            assert len(result) == 1
            assert result[0]['name'] == 'John Doe'
            assert result[0]['position'] == 'Backend Developer'
            assert result[0]['performance'] == '4.8'
        finally:
            os.unlink(temp_path)

    def test_read_csv_file_with_multiple_rows(self):
        """Тест чтения CSV файла с несколькими строками"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f.write('John Doe,Backend Developer,45,4.8,"Python, Django",API Team,5\n')
            f.write('Jane Smith,Frontend Developer,38,4.7,"React, TypeScript",Web Team,4\n')
            temp_path = f.name

        try:
            result = read_csv_file(temp_path)
            assert len(result) == 2
            assert result[0]['name'] == 'John Doe'
            assert result[1]['name'] == 'Jane Smith'
        finally:
            os.unlink(temp_path)

    def test_read_csv_file_not_found(self):
        """Тест обработки ошибки когда файл не найден"""
        with pytest.raises(FileNotFoundError) as exc_info:
            read_csv_file("nonexistent_file.csv")
        assert "Файл не найден" in str(exc_info.value)

    def test_read_csv_file_path_is_directory(self):
        """Тест обработки ошибки когда путь указывает на директорию"""
        with tempfile.TemporaryDirectory() as temp_dir:
            with pytest.raises(FileNotFoundError) as exc_info:
                read_csv_file(temp_dir)
            assert "Путь не является файлом" in str(exc_info.value)

    def test_read_csv_file_invalid_format(self):
        """Тест обработки ошибки при невалидном формате CSV"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('invalid csv content without proper format\n')
            temp_path = f.name

        try:
            # CSV может быть прочитан, но с пустыми значениями или ошибками
            # Проверяем что функция не падает с критической ошибкой
            result = read_csv_file(temp_path)
            # Результат может быть пустым или содержать некорректные данные
            assert isinstance(result, list)
        finally:
            os.unlink(temp_path)



class TestReadCsvFiles:
    """Тесты для функции read_csv_files"""

    def test_read_multiple_files(self):
        """Тест чтения нескольких файлов"""
        # Создаем два временных файла
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
            f1.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f1.write('John Doe,Backend Developer,45,4.8,"Python",API Team,5\n')
            temp_path1 = f1.name

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
            f2.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f2.write('Jane Smith,Frontend Developer,38,4.7,"React",Web Team,4\n')
            temp_path2 = f2.name

        try:
            result = read_csv_files([temp_path1, temp_path2])
            assert len(result) == 2
            assert result[0]['name'] == 'John Doe'
            assert result[1]['name'] == 'Jane Smith'
        finally:
            os.unlink(temp_path1)
            os.unlink(temp_path2)

    def test_read_multiple_files_with_duplicates(self):
        """Тест чтения нескольких файлов с одинаковыми позициями"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
            f1.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f1.write('John Doe,Backend Developer,45,4.8,"Python",API Team,5\n')
            temp_path1 = f1.name

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
            f2.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f2.write('Bob Wilson,Backend Developer,50,4.9,"Go",API Team,6\n')
            temp_path2 = f2.name

        try:
            result = read_csv_files([temp_path1, temp_path2])
            assert len(result) == 2
            assert all(emp['position'] == 'Backend Developer' for emp in result)
        finally:
            os.unlink(temp_path1)
            os.unlink(temp_path2)

    def test_read_csv_files_one_file_not_found(self):
        """Тест обработки ошибки когда один из файлов не найден"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,position,completed_tasks,performance,skills,team,experience_years\n')
            f.write('John Doe,Backend Developer,45,4.8,"Python",API Team,5\n')
            temp_path = f.name

        try:
            with pytest.raises(FileNotFoundError):
                read_csv_files([temp_path, "nonexistent_file.csv"])
        finally:
            os.unlink(temp_path)

    def test_read_csv_files_empty_list(self):
        """Тест чтения пустого списка файлов"""
        result = read_csv_files([])
        assert result == []

