import pytest
from performance_review import calculate_average_performance, generate_performance_table


class TestCalculateAveragePerformance:
    """Тесты для функции calculate_average_performance"""

    def test_calculate_average_single_position(self):
        """Тест расчета среднего для одной позиции"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            },
            {
                'name': 'Jane Smith',
                'position': 'Backend Developer',
                'performance': '4.6',
                'completed_tasks': '40'
            }
        ]
        result = calculate_average_performance(employees)
        assert 'Backend Developer' in result
        assert result['Backend Developer'] == pytest.approx(4.7, abs=0.01)

    def test_calculate_average_multiple_positions(self):
        """Тест расчета среднего для нескольких позиций"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            },
            {
                'name': 'Jane Smith',
                'position': 'Frontend Developer',
                'performance': '4.7',
                'completed_tasks': '38'
            },
            {
                'name': 'Bob Wilson',
                'position': 'Backend Developer',
                'performance': '4.9',
                'completed_tasks': '50'
            }
        ]
        result = calculate_average_performance(employees)
        assert len(result) == 2
        assert 'Backend Developer' in result
        assert 'Frontend Developer' in result
        # Backend: (4.8 + 4.9) / 2 = 4.85
        assert result['Backend Developer'] == pytest.approx(4.85, abs=0.01)
        assert result['Frontend Developer'] == pytest.approx(4.7, abs=0.01)

    def test_calculate_average_empty_list(self):
        """Тест расчета среднего для пустого списка"""
        result = calculate_average_performance([])
        assert result == {}

    def test_calculate_average_missing_position(self):
        """Тест обработки записей без поля position"""
        employees = [
            {
                'name': 'John Doe',
                'performance': '4.8',
                'completed_tasks': '45'
            }
        ]
        result = calculate_average_performance(employees)
        assert result == {}

    def test_calculate_average_missing_performance(self):
        """Тест обработки записей без поля performance"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'completed_tasks': '45'
            }
        ]
        result = calculate_average_performance(employees)
        assert result == {}

    def test_calculate_average_empty_position(self):
        """Тест обработки записей с пустым position"""
        employees = [
            {
                'name': 'John Doe',
                'position': '',
                'performance': '4.8',
                'completed_tasks': '45'
            }
        ]
        result = calculate_average_performance(employees)
        assert result == {}

    def test_calculate_average_empty_performance(self):
        """Тест обработки записей с пустым performance"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '',
                'completed_tasks': '45'
            }
        ]
        result = calculate_average_performance(employees)
        assert result == {}

    def test_calculate_average_invalid_performance_value(self):
        """Тест обработки некорректного значения performance"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': 'invalid',
                'completed_tasks': '45'
            }
        ]
        with pytest.raises(Exception) as exc_info:
            calculate_average_performance(employees)
        assert "Ошибка во время подсчета average performance" in str(exc_info.value)

    def test_calculate_average_real_data(self):
        """Тест с реальными данными из примера"""
        employees = [
            {
                'name': 'Alex Ivanov',
                'position': 'Backend Developer',
                'completed_tasks': '45',
                'performance': '4.8',
                'skills': 'Python, Django, PostgreSQL, Docker',
                'team': 'API Team',
                'experience_years': '5'
            },
            {
                'name': 'Tom Anderson',
                'position': 'Backend Developer',
                'completed_tasks': '49',
                'performance': '4.9',
                'skills': 'Go, Microservices, gRPC, PostgreSQL',
                'team': 'API Team',
                'experience_years': '7'
            },
            {
                'name': 'Maria Petrova',
                'position': 'Frontend Developer',
                'completed_tasks': '38',
                'performance': '4.7',
                'skills': 'React, TypeScript, Redux, CSS',
                'team': 'Web Team',
                'experience_years': '4'
            }
        ]
        result = calculate_average_performance(employees)
        # Backend: (4.8 + 4.9) / 2 = 4.85
        assert result['Backend Developer'] == pytest.approx(4.85, abs=0.01)
        assert result['Frontend Developer'] == pytest.approx(4.7, abs=0.01)


class TestGeneratePerformanceTable:
    """Тесты для функции generate_performance_table"""

    def test_generate_table_single_position(self):
        """Тест генерации таблицы для одной позиции"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            }
        ]
        table = generate_performance_table(employees)
        assert isinstance(table, str)
        assert 'Backend Developer' in table
        assert '4.80' in table or '4.8' in table
        assert 'position' in table.lower()
        assert 'performance' in table.lower()

    def test_generate_table_multiple_positions_sorted(self):
        """Тест генерации таблицы с сортировкой по убыванию"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            },
            {
                'name': 'Jane Smith',
                'position': 'Frontend Developer',
                'performance': '4.9',
                'completed_tasks': '50'
            },
            {
                'name': 'Bob Wilson',
                'position': 'QA Engineer',
                'performance': '4.5',
                'completed_tasks': '40'
            }
        ]
        table = generate_performance_table(employees)
        assert isinstance(table, str)
        # Проверяем что таблица отсортирована по убыванию
        # Frontend (4.9) должен быть первым, затем Backend (4.8), затем QA (4.5)
        frontend_index = table.find('Frontend Developer')
        backend_index = table.find('Backend Developer')
        qa_index = table.find('QA Engineer')
        
        assert frontend_index < backend_index
        assert backend_index < qa_index

    def test_generate_table_empty_list(self):
        """Тест генерации таблицы для пустого списка"""
        table = generate_performance_table([])
        assert isinstance(table, str)
        # Таблица должна содержать заголовки даже для пустых данных
        assert 'position' in table.lower() or len(table) > 0

    def test_generate_table_format(self):
        """Тест формата таблицы"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            }
        ]
        table = generate_performance_table(employees)
        # Таблица должна содержать заголовки
        lines = table.split('\n')
        assert len(lines) >= 2  # Заголовок + минимум одна строка данных

    def test_generate_table_real_data(self):
        """Тест генерации таблицы с реальными данными"""
        employees = [
            {
                'name': 'Alex Ivanov',
                'position': 'Backend Developer',
                'completed_tasks': '45',
                'performance': '4.8',
                'skills': 'Python, Django, PostgreSQL, Docker',
                'team': 'API Team',
                'experience_years': '5'
            },
            {
                'name': 'Anna Lee',
                'position': 'DevOps Engineer',
                'completed_tasks': '52',
                'performance': '4.9',
                'skills': 'AWS, Kubernetes, Terraform, Ansible',
                'team': 'Infrastructure Team',
                'experience_years': '6'
            },
            {
                'name': 'Mike Brown',
                'position': 'QA Engineer',
                'completed_tasks': '41',
                'performance': '4.5',
                'skills': 'Selenium, Jest, Cypress, Postman',
                'team': 'Testing Team',
                'experience_years': '4'
            }
        ]
        table = generate_performance_table(employees)
        assert isinstance(table, str)
        assert 'DevOps Engineer' in table
        assert 'Backend Developer' in table
        assert 'QA Engineer' in table

    def test_generate_table_tabulate_error(self):
        """Тест обработки ошибки при генерации таблицы через tabulate"""
        employees = [
            {
                'name': 'John Doe',
                'position': 'Backend Developer',
                'performance': '4.8',
                'completed_tasks': '45'
            }
        ]
        # Мокаем tabulate чтобы вызвать исключение
        from unittest.mock import patch
        with patch('performance_review.tabulate.tabulate') as mock_tabulate:
            mock_tabulate.side_effect = Exception("Ошибка tabulate")
            with pytest.raises(Exception) as exc_info:
                generate_performance_table(employees)
            assert "Ошибка при преобразовании в таблицу" in str(exc_info.value)

