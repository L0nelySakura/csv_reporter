import tabulate


def calculate_average_performance(employees: list[dict[str, str]]) -> dict[str, float]:
    position_performance = {}
    for employee in employees:
        pos = employee.get("position")
        perf = employee.get("performance")
        if pos and perf:
            if pos not in position_performance.keys():
                position_performance[pos] = []
            position_performance[pos].append(float(perf))

    avg_perf = {}
    for pos_key, perf_value in position_performance.items():
        if perf_value:
            avg_perf[pos_key] = sum(perf_value) / len(perf_value)

    return avg_perf


def generate_performance_table(employees: list[dict[str, str]]):

    sorted_positions = sorted(
        calculate_average_performance(employees=employees).items(),
        key=lambda x: -x[1]
    )

    table = tabulate.tabulate(
        sorted_positions,
        headers=['position', 'performance'],
        floatfmt=".2f"
    )

    return table


if __name__ == "__main__":
    print(calculate_average_performance([{'name': 'David Chen', 'position': 'Mobile Developer', 'completed_tasks': '36', 'performance': '4.6', 'skills': 'Swift, Kotlin, React Native, iOS', 'team': 'Mobile Team', 'experience_years': '3'}, {'name': 'Elena Popova', 'position': 'Backend Developer', 'completed_tasks': '43', 'performance': '4.8', 'skills': 'Java, Spring Boot, MySQL, Redis', 'team': 'API Team', 'experience_years': '4'}, {'name': 'Chris Wilson', 'position': 'DevOps Engineer', 'completed_tasks': '39', 'performance': '4.7', 'skills': 'Docker, Jenkins, GitLab CI, AWS', 'team': 'Infrastructure Team', 'experience_years': '5'}, {'name': 'Olga Kuznetsova', 'position': 'Frontend Developer', 'completed_tasks': '42', 'performance': '4.6', 'skills': 'Vue.js, JavaScript, Webpack, Sass', 'team': 'Web Team', 'experience_years': '3'}, {'name': 'Robert Kim', 'position': 'Data Engineer', 'completed_tasks': '34', 'performance': '4.7', 'skills': 'Python, Apache Spark, Airflow, Kafka', 'team': 'Data Team', 'experience_years': '4'}, {'name': 'Julia Martin', 'position': 'QA Engineer', 'completed_tasks': '38', 'performance': '4.5', 'skills': 'Playwright, Jest, API Testing', 'team': 'Testing Team', 'experience_years': '3'}, {'name': 'Tom Anderson', 'position': 'Backend Developer', 'completed_tasks': '49', 'performance': '4.9', 'skills': 'Go, Microservices, gRPC, PostgreSQL', 'team': 'API Team', 'experience_years': '7'}, {'name': 'Lisa Wang', 'position': 'Mobile Developer', 'completed_tasks': '33', 'performance': '4.6', 'skills': 'Flutter, Dart, Android, Firebase', 'team': 'Mobile Team', 'experience_years': '2'}, {'name': 'Mark Thompson', 'position': 'Data Scientist', 'completed_tasks': '31', 'performance': '4.7', 'skills': 'R, Python, TensorFlow, SQL', 'team': 'AI Team', 'experience_years': '4'}]))
    print(calculate_average_performance(
        [{'name': 'David Chen', 'position': 'Mobile Developer', 'completed_tasks': '36', 'performance': '4.6',
          'skills': 'Swift, Kotlin, React Native, iOS', 'team': 'Mobile Team', 'experience_years': '3'},
         {'name': 'Elena Popova', 'position': 'Backend Developer', 'completed_tasks': '43', 'performance': '4.8',
          'skills': 'Java, Spring Boot, MySQL, Redis', 'team': 'API Team', 'experience_years': '4'},
         {'name': 'Chris Wilson', 'position': 'DevOps Engineer', 'completed_tasks': '39', 'performance': '4.7',
          'skills': 'Docker, Jenkins, GitLab CI, AWS', 'team': 'Infrastructure Team', 'experience_years': '5'},
         {'name': 'Olga Kuznetsova', 'position': 'Frontend Developer', 'completed_tasks': '42', 'performance': '4.6',
          'skills': 'Vue.js, JavaScript, Webpack, Sass', 'team': 'Web Team', 'experience_years': '3'},
         {'name': 'Robert Kim', 'position': 'Data Engineer', 'completed_tasks': '34', 'performance': '4.7',
          'skills': 'Python, Apache Spark, Airflow, Kafka', 'team': 'Data Team', 'experience_years': '4'},
         {'name': 'Julia Martin', 'position': 'QA Engineer', 'completed_tasks': '38', 'performance': '4.5',
          'skills': 'Playwright, Jest, API Testing', 'team': 'Testing Team', 'experience_years': '3'},
         {'name': 'Tom Anderson', 'position': 'Backend Developer', 'completed_tasks': '49', 'performance': '4.9',
          'skills': 'Go, Microservices, gRPC, PostgreSQL', 'team': 'API Team', 'experience_years': '7'},
         {'name': 'Lisa Wang', 'position': 'Mobile Developer', 'completed_tasks': '33', 'performance': '4.6',
          'skills': 'Flutter, Dart, Android, Firebase', 'team': 'Mobile Team', 'experience_years': '2'},
         {'name': 'Mark Thompson', 'position': 'Data Scientist', 'completed_tasks': '31', 'performance': '4.7',
          'skills': 'R, Python, TensorFlow, SQL', 'team': 'AI Team', 'experience_years': '4'},
         {'name': 'Alex Ivanov', 'position': 'Backend Developer', 'completed_tasks': '45', 'performance': '4.8',
          'skills': 'Python, Django, PostgreSQL, Docker', 'team': 'API Team', 'experience_years': '5'},
         {'name': 'Maria Petrova', 'position': 'Frontend Developer', 'completed_tasks': '38', 'performance': '4.7',
          'skills': 'React, TypeScript, Redux, CSS', 'team': 'Web Team', 'experience_years': '4'},
         {'name': 'John Smith', 'position': 'Data Scientist', 'completed_tasks': '29', 'performance': '4.6',
          'skills': 'Python, ML, SQL, Pandas', 'team': 'AI Team', 'experience_years': '3'},
         {'name': 'Anna Lee', 'position': 'DevOps Engineer', 'completed_tasks': '52', 'performance': '4.9',
          'skills': 'AWS, Kubernetes, Terraform, Ansible', 'team': 'Infrastructure Team', 'experience_years': '6'},
         {'name': 'Mike Brown', 'position': 'QA Engineer', 'completed_tasks': '41', 'performance': '4.5',
          'skills': 'Selenium, Jest, Cypress, Postman', 'team': 'Testing Team', 'experience_years': '4'},
         {'name': 'Sarah Johnson', 'position': 'Fullstack Developer', 'completed_tasks': '47', 'performance': '4.7',
          'skills': 'JavaScript, Node.js, React, MongoDB', 'team': 'Web Team', 'experience_years': '5'}]
    ))
    print(generate_performance_table([{'name': 'David Chen', 'position': 'Mobile Developer', 'completed_tasks': '36',
                                          'performance': '4.6', 'skills': 'Swift, Kotlin, React Native, iOS',
                                          'team': 'Mobile Team', 'experience_years': '3'},
                                         {'name': 'Elena Popova', 'position': 'Backend Developer',
                                          'completed_tasks': '43', 'performance': '4.8',
                                          'skills': 'Java, Spring Boot, MySQL, Redis', 'team': 'API Team',
                                          'experience_years': '4'},
                                         {'name': 'Chris Wilson', 'position': 'DevOps Engineer',
                                          'completed_tasks': '39', 'performance': '4.7',
                                          'skills': 'Docker, Jenkins, GitLab CI, AWS', 'team': 'Infrastructure Team',
                                          'experience_years': '5'},
                                         {'name': 'Olga Kuznetsova', 'position': 'Frontend Developer',
                                          'completed_tasks': '42', 'performance': '4.6',
                                          'skills': 'Vue.js, JavaScript, Webpack, Sass', 'team': 'Web Team',
                                          'experience_years': '3'},
                                         {'name': 'Robert Kim', 'position': 'Data Engineer', 'completed_tasks': '34',
                                          'performance': '4.7', 'skills': 'Python, Apache Spark, Airflow, Kafka',
                                          'team': 'Data Team', 'experience_years': '4'},
                                         {'name': 'Julia Martin', 'position': 'QA Engineer', 'completed_tasks': '38',
                                          'performance': '4.5', 'skills': 'Playwright, Jest, API Testing',
                                          'team': 'Testing Team', 'experience_years': '3'},
                                         {'name': 'Tom Anderson', 'position': 'Backend Developer',
                                          'completed_tasks': '49', 'performance': '4.9',
                                          'skills': 'Go, Microservices, gRPC, PostgreSQL', 'team': 'API Team',
                                          'experience_years': '7'},
                                         {'name': 'Lisa Wang', 'position': 'Mobile Developer', 'completed_tasks': '33',
                                          'performance': '4.6', 'skills': 'Flutter, Dart, Android, Firebase',
                                          'team': 'Mobile Team', 'experience_years': '2'},
                                         {'name': 'Mark Thompson', 'position': 'Data Scientist',
                                          'completed_tasks': '31', 'performance': '4.7',
                                          'skills': 'R, Python, TensorFlow, SQL', 'team': 'AI Team',
                                          'experience_years': '4'}]))
    print(generate_performance_table(
        [{'name': 'David Chen', 'position': 'Mobile Developer', 'completed_tasks': '36', 'performance': '4.6',
          'skills': 'Swift, Kotlin, React Native, iOS', 'team': 'Mobile Team', 'experience_years': '3'},
         {'name': 'Elena Popova', 'position': 'Backend Developer', 'completed_tasks': '43', 'performance': '4.8',
          'skills': 'Java, Spring Boot, MySQL, Redis', 'team': 'API Team', 'experience_years': '4'},
         {'name': 'Chris Wilson', 'position': 'DevOps Engineer', 'completed_tasks': '39', 'performance': '4.7',
          'skills': 'Docker, Jenkins, GitLab CI, AWS', 'team': 'Infrastructure Team', 'experience_years': '5'},
         {'name': 'Olga Kuznetsova', 'position': 'Frontend Developer', 'completed_tasks': '42', 'performance': '4.6',
          'skills': 'Vue.js, JavaScript, Webpack, Sass', 'team': 'Web Team', 'experience_years': '3'},
         {'name': 'Robert Kim', 'position': 'Data Engineer', 'completed_tasks': '34', 'performance': '4.7',
          'skills': 'Python, Apache Spark, Airflow, Kafka', 'team': 'Data Team', 'experience_years': '4'},
         {'name': 'Julia Martin', 'position': 'QA Engineer', 'completed_tasks': '38', 'performance': '4.5',
          'skills': 'Playwright, Jest, API Testing', 'team': 'Testing Team', 'experience_years': '3'},
         {'name': 'Tom Anderson', 'position': 'Backend Developer', 'completed_tasks': '49', 'performance': '4.9',
          'skills': 'Go, Microservices, gRPC, PostgreSQL', 'team': 'API Team', 'experience_years': '7'},
         {'name': 'Lisa Wang', 'position': 'Mobile Developer', 'completed_tasks': '33', 'performance': '4.6',
          'skills': 'Flutter, Dart, Android, Firebase', 'team': 'Mobile Team', 'experience_years': '2'},
         {'name': 'Mark Thompson', 'position': 'Data Scientist', 'completed_tasks': '31', 'performance': '4.7',
          'skills': 'R, Python, TensorFlow, SQL', 'team': 'AI Team', 'experience_years': '4'},
         {'name': 'Alex Ivanov', 'position': 'Backend Developer', 'completed_tasks': '45', 'performance': '4.8',
          'skills': 'Python, Django, PostgreSQL, Docker', 'team': 'API Team', 'experience_years': '5'},
         {'name': 'Maria Petrova', 'position': 'Frontend Developer', 'completed_tasks': '38', 'performance': '4.7',
          'skills': 'React, TypeScript, Redux, CSS', 'team': 'Web Team', 'experience_years': '4'},
         {'name': 'John Smith', 'position': 'Data Scientist', 'completed_tasks': '29', 'performance': '4.6',
          'skills': 'Python, ML, SQL, Pandas', 'team': 'AI Team', 'experience_years': '3'},
         {'name': 'Anna Lee', 'position': 'DevOps Engineer', 'completed_tasks': '52', 'performance': '4.9',
          'skills': 'AWS, Kubernetes, Terraform, Ansible', 'team': 'Infrastructure Team', 'experience_years': '6'},
         {'name': 'Mike Brown', 'position': 'QA Engineer', 'completed_tasks': '41', 'performance': '4.5',
          'skills': 'Selenium, Jest, Cypress, Postman', 'team': 'Testing Team', 'experience_years': '4'},
         {'name': 'Sarah Johnson', 'position': 'Fullstack Developer', 'completed_tasks': '47', 'performance': '4.7',
          'skills': 'JavaScript, Node.js, React, MongoDB', 'team': 'Web Team', 'experience_years': '5'}]
    ))
