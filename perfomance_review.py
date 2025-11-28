from collections import defaultdict


def calculate_review(employees):
    position_performance = {}
    for employee in employees:
        position = employee.get("position")
        performance = employee.get("performance")
        if position and performance:
            if position not in position_performance.keys():
                position_performance[position] = []
            position_performance[position].append(float(performance))

    average_performance = {}
    for position_key, performances_value in position_performance.items():
        if performances_value:
            average_performance[position_key] = sum(performances_value) / len(performances_value)

    return average_performance


if __name__ == "__main__":
    print(calculate_review([{'name': 'David Chen', 'position': 'Mobile Developer', 'completed_tasks': '36', 'performance': '4.6', 'skills': 'Swift, Kotlin, React Native, iOS', 'team': 'Mobile Team', 'experience_years': '3'}, {'name': 'Elena Popova', 'position': 'Backend Developer', 'completed_tasks': '43', 'performance': '4.8', 'skills': 'Java, Spring Boot, MySQL, Redis', 'team': 'API Team', 'experience_years': '4'}, {'name': 'Chris Wilson', 'position': 'DevOps Engineer', 'completed_tasks': '39', 'performance': '4.7', 'skills': 'Docker, Jenkins, GitLab CI, AWS', 'team': 'Infrastructure Team', 'experience_years': '5'}, {'name': 'Olga Kuznetsova', 'position': 'Frontend Developer', 'completed_tasks': '42', 'performance': '4.6', 'skills': 'Vue.js, JavaScript, Webpack, Sass', 'team': 'Web Team', 'experience_years': '3'}, {'name': 'Robert Kim', 'position': 'Data Engineer', 'completed_tasks': '34', 'performance': '4.7', 'skills': 'Python, Apache Spark, Airflow, Kafka', 'team': 'Data Team', 'experience_years': '4'}, {'name': 'Julia Martin', 'position': 'QA Engineer', 'completed_tasks': '38', 'performance': '4.5', 'skills': 'Playwright, Jest, API Testing', 'team': 'Testing Team', 'experience_years': '3'}, {'name': 'Tom Anderson', 'position': 'Backend Developer', 'completed_tasks': '49', 'performance': '4.9', 'skills': 'Go, Microservices, gRPC, PostgreSQL', 'team': 'API Team', 'experience_years': '7'}, {'name': 'Lisa Wang', 'position': 'Mobile Developer', 'completed_tasks': '33', 'performance': '4.6', 'skills': 'Flutter, Dart, Android, Firebase', 'team': 'Mobile Team', 'experience_years': '2'}, {'name': 'Mark Thompson', 'position': 'Data Scientist', 'completed_tasks': '31', 'performance': '4.7', 'skills': 'R, Python, TensorFlow, SQL', 'team': 'AI Team', 'experience_years': '4'}]))