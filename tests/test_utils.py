from src.utils import (
    filter_by_description,
    get_top_n_vacancies,
    range_vacancies_by_salary,
    sort_vacancies,
    print_vacancies,
)
from src.vacancy import Vacancy


def test_filter_by_description(vacancies_list):
    filtered_vacancies = filter_by_description(vacancies_list, ["SQL", "Java"])
    assert len(filtered_vacancies) == 3


def test_range_vacancies_by_salary(vacancies_list):
    ranged_vacancies = range_vacancies_by_salary(vacancies_list, "300-600")
    assert ranged_vacancies[0].salary == {"from": 400, "to": 600, "currency": "RUR"}
    assert ranged_vacancies[1].salary == {"from": 300, "to": 400, "currency": "RUR"}


def test_range_vacancies_by_salary_empty():
    assert range_vacancies_by_salary([], "100-500") == []


def test_get_top_3_vacancies(vacancies_list):
    top_3 = get_top_n_vacancies(vacancies_list, 3)
    assert len(top_3) == 3


def test_get_top_n_vacancies_more(vacancies_list):
    top_n = get_top_n_vacancies(vacancies_list, 7)
    assert len(top_n) == 5


def test_sort_vacancies(vacancies_list):
    sorted_vacancies = sort_vacancies(vacancies_list)
    assert sorted_vacancies[0].salary == {"from": 400, "to": 600, "currency": "RUR"}
    assert sorted_vacancies[-1].salary == {"from": 100, "to": 0, "currency": "RUR"}


def test_print_vacancies(capsys, vacancy_1, vacancy_2, vacancy_3):
    test_list = [Vacancy(vacancy_1), Vacancy(vacancy_2), Vacancy(vacancy_3)]
    print_vacancies(test_list)
    printed_vacancies = capsys.readouterr()
    assert (
        printed_vacancies.out.strip()
        == """Vacancy #1:
        name: Python developer
        salary: От 100 до 300 руб.
        requirement: SQL
        url: test_url
Vacancy #2:
        name: Java developer
        salary: До 300 руб.
        requirement: Java
        url: test_url
Vacancy #3:
        name: DevOps
        salary: От 100 руб.
        requirement: Management skills
        url: test_url"""
    )
