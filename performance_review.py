import tabulate


def calculate_average_performance(employees: list[dict[str, str]]) -> dict[str, float]:
    try:
        position_performance = {}
        for employee in employees:
            pos = employee.get("position")
            perf = employee.get("performance")
            if pos and perf:
                if pos not in position_performance:
                    position_performance[pos] = []
                position_performance[pos].append(float(perf))

        avg_perf = {}
        for pos_key, perf_value in position_performance.items():
            if perf_value:
                avg_perf[pos_key] = sum(perf_value) / len(perf_value)
    except Exception as e:
        raise Exception(f"Ошибка во время подсчета average performance: {e}")
    return avg_perf


def generate_performance_table(employees: list[dict[str, str]]):
    sorted_positions = sorted(
        calculate_average_performance(employees=employees).items(),
        key=lambda x: -x[1]
    )
    try:
        table = tabulate.tabulate(
            sorted_positions,
            headers=['position', 'performance'],
            floatfmt=".2f"
        )
    except Exception as e:
        raise Exception(f"Ошибка при преобразовании в таблицу: {e}")

    return table

