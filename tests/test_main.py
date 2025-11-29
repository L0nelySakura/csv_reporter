import pytest
import sys
from unittest.mock import patch, MagicMock
from main import parse_arguments, main


class TestParseArguments:
    """Тесты для функции parse_arguments"""

    def test_parse_arguments_valid(self):
        """Тест парсинга валидных аргументов"""
        test_args = ['--files', 'file1.csv', 'file2.csv', '--report', 'performance']
        with patch('sys.argv', ['main.py'] + test_args):
            args = parse_arguments()
            assert args.files == ['file1.csv', 'file2.csv']
            assert args.report == 'performance'

    def test_parse_arguments_single_file(self):
        """Тест парсинга одного файла"""
        test_args = ['--files', 'file1.csv', '--report', 'performance']
        with patch('sys.argv', ['main.py'] + test_args):
            args = parse_arguments()
            assert args.files == ['file1.csv']
            assert args.report == 'performance'

    def test_parse_arguments_multiple_files(self):
        """Тест парсинга нескольких файлов"""
        test_args = ['--files', 'file1.csv', 'file2.csv', 'file3.csv', '--report', 'performance']
        with patch('sys.argv', ['main.py'] + test_args):
            args = parse_arguments()
            assert len(args.files) == 3
            assert 'file1.csv' in args.files
            assert 'file2.csv' in args.files
            assert 'file3.csv' in args.files


class TestMain:
    """Интеграционные тесты для функции main"""

    @patch('main.generate_performance_table')
    @patch('main.read_csv_files')
    @patch('main.parse_arguments')
    @patch('builtins.print')
    def test_main_performance_report_success(self, mock_print, mock_parse, mock_read, mock_generate):
        """Тест успешного выполнения с отчетом performance"""
        # Настройка моков
        mock_args = MagicMock()
        mock_args.files = ['file1.csv', 'file2.csv']
        mock_args.report = 'performance'
        mock_parse.return_value = mock_args
        
        mock_employees = [
            {'name': 'John Doe', 'position': 'Backend Developer', 'performance': '4.8'}
        ]
        mock_read.return_value = mock_employees
        
        mock_table = "position               performance\n-------------------  -------------\nBackend Developer             4.80"
        mock_generate.return_value = mock_table
        
        # Вызов функции
        main()
        
        # Проверки
        mock_parse.assert_called_once()
        mock_read.assert_called_once_with(['file1.csv', 'file2.csv'])
        mock_generate.assert_called_once_with(mock_employees)
        mock_print.assert_called_once_with(mock_table)

    @patch('main.parse_arguments')
    @patch('main.read_csv_files')
    def test_main_file_not_found(self, mock_read, mock_parse):
        """Тест обработки ошибки FileNotFoundError"""
        mock_args = MagicMock()
        mock_args.files = ['nonexistent.csv']
        mock_args.report = 'performance'
        mock_parse.return_value = mock_args
        
        mock_read.side_effect = FileNotFoundError("Файл не найден: nonexistent.csv")
        
        with patch('builtins.print') as mock_print:
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit(1)
                with pytest.raises(SystemExit):
                    main()
                mock_print.assert_called()
                assert "Ошибка при чтении файлов" in str(mock_print.call_args[0][0])
                mock_exit.assert_called_once_with(1)

    @patch('main.parse_arguments')
    @patch('main.read_csv_files')
    def test_main_permission_error(self, mock_read, mock_parse):
        """Тест обработки ошибки PermissionError"""
        mock_args = MagicMock()
        mock_args.files = ['file.csv']
        mock_args.report = 'performance'
        mock_parse.return_value = mock_args
        
        mock_read.side_effect = PermissionError("Доступ запрещен")
        
        with patch('builtins.print') as mock_print:
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit(1)
                with pytest.raises(SystemExit):
                    main()
                mock_print.assert_called()
                assert "Ошибка при чтении файлов" in str(mock_print.call_args[0][0])
                mock_exit.assert_called_once_with(1)

    @patch('main.parse_arguments')
    @patch('main.read_csv_files')
    @patch('sys.exit')
    def test_main_unknown_report(self, mock_exit, mock_read, mock_parse):
        """Тест обработки неизвестного типа отчета"""
        mock_args = MagicMock()
        mock_args.files = ['file1.csv']
        mock_args.report = 'unknown_report'
        mock_parse.return_value = mock_args
        
        mock_read.return_value = [{'name': 'John Doe', 'position': 'Backend Developer', 'performance': '4.8'}]
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called()
            assert "Неизвестный/нереализованный тип отчёта" in str(mock_print.call_args)

    @patch('main.parse_arguments')
    def test_main_critical_error(self, mock_parse):
        """Тест обработки критической ошибки"""
        mock_parse.side_effect = Exception("Критическая ошибка")
        
        with patch('builtins.print') as mock_print:
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit(1)
                with pytest.raises(SystemExit):
                    main()
                mock_print.assert_called()
                assert "Критическая ошибка" in str(mock_print.call_args[0][0])
                mock_exit.assert_called_once_with(1)

    @patch('main.parse_arguments')
    @patch('main.read_csv_files')
    def test_main_generate_table_error(self, mock_read, mock_parse):
        """Тест обработки ошибки при генерации таблицы"""
        mock_args = MagicMock()
        mock_args.files = ['file1.csv']
        mock_args.report = 'performance'
        mock_parse.return_value = mock_args
        
        mock_read.return_value = [{'name': 'John Doe', 'position': 'Backend Developer', 'performance': '4.8'}]
        
        with patch('main.generate_performance_table') as mock_generate:
            mock_generate.side_effect = Exception("Ошибка генерации таблицы")
            
            with patch('builtins.print') as mock_print:
                with patch('sys.exit') as mock_exit:
                    mock_exit.side_effect = SystemExit(1)
                    with pytest.raises(SystemExit):
                        main()
                    # Ошибка должна быть обработана в main
                    mock_exit.assert_called_once_with(1)

    @patch('main.parse_arguments')
    @patch('main.read_csv_files')
    def test_main_read_files_general_exception(self, mock_read, mock_parse):
        """Тест обработки общего Exception при чтении файлов"""
        mock_args = MagicMock()
        mock_args.files = ['file1.csv']
        mock_args.report = 'performance'
        mock_parse.return_value = mock_args
        
        # Вызываем общий Exception, не FileNotFoundError и не PermissionError
        mock_read.side_effect = ValueError("Неизвестная ошибка")
        
        with patch('builtins.print') as mock_print:
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit(1)
                with pytest.raises(SystemExit):
                    main()
                mock_print.assert_called()
                assert "Неизвестная ошибка при чтении файлов" in str(mock_print.call_args[0][0])
                mock_exit.assert_called_once_with(1)

