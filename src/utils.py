def filter_by_description(vacancies: list, filter_words: list) -> list:
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in filter_words:
            if word.lower() in vacancy.requirement.lower():
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def range_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    if vacancies:
        min_salary, max_salary = list(map(int, salary_range.split("-")))
        return list(
            filter(
                lambda x: min_salary
                <= x.salary["from"]
                <= (x.salary["from"] if x.salary["to"] == 0 else x.salary["to"])
                <= max_salary,
                vacancies,
            )
        )
    return []


def get_top_n_vacancies(vacancies: list, top_n: int) -> list:
    if len(vacancies) > top_n:
        return vacancies[:top_n]
    else:
        return vacancies


def sort_vacancies(vacancies: list) -> list:
    return sorted(vacancies, reverse=True)


def print_vacancies(vacancies: list) -> None:
    for index, vacancy in enumerate(vacancies, 1):
        if vacancy.salary["from"] == 0:
            salary = f"До {vacancy.salary['to']} руб."
        elif vacancy.salary["to"] == 0:
            salary = f"От {vacancy.salary['from']} руб."
        else:
            salary = f"От {vacancy.salary['from']} до {vacancy.salary['to']} руб."
        print(
            f"""Vacancy #{index}:
        name: {vacancy.name}
        salary: {salary}
        requirement: {vacancy.requirement}
        url: {vacancy.url}"""
        )
