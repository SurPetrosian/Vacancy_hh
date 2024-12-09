from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    new_vacancy = Vacancy(vacancy_1)
    assert new_vacancy.name == "Python developer"
    assert new_vacancy.salary == {"from": 100, "to": 300, "currency": "RUR"}
    assert new_vacancy.url == "test_url"
    assert new_vacancy.requirement == "SQL"
    assert new_vacancy.vacancy_info == {
        "name": "Python developer",
        "salary": {"from": 100, "to": 300, "currency": "RUR"},
        "url": "test_url",
        "requirement": "SQL",
    }


def test_vacancy_init_none(vacancy_2, vacancy_3, vacancy_5):
    new_vacancy_1 = Vacancy(vacancy_2)
    new_vacancy_2 = Vacancy(vacancy_3)
    new_vacancy_3 = Vacancy(vacancy_5)
    assert new_vacancy_1.salary == {"from": 0, "to": 300, "currency": "RUR"}
    assert new_vacancy_2.salary == {"from": 100, "to": 0, "currency": "RUR"}
    assert new_vacancy_3.requirement == "No information"


def test_add_vacancy_to_list(vacancy_1, vacancy_2, vacancy_3):
    new_vacancy_1 = Vacancy(vacancy_1)
    new_vacancy_2 = Vacancy(vacancy_2)
    new_vacancy_3 = Vacancy(vacancy_3)
    Vacancy.cast_vacancies_to_list(new_vacancy_1)
    Vacancy.cast_vacancies_to_list(new_vacancy_2)
    Vacancy.cast_vacancies_to_list(new_vacancy_3)
    assert len(new_vacancy_1) == 3


def test_compare_salaries(vacancy_1, vacancy_2, vacancy_3):
    new_vacancy_1 = Vacancy(vacancy_1)
    new_vacancy_2 = Vacancy(vacancy_2)
    new_vacancy_3 = Vacancy(vacancy_3)
    assert new_vacancy_2 > new_vacancy_3
    assert new_vacancy_3 < new_vacancy_1
    assert new_vacancy_1 >= new_vacancy_2
    assert new_vacancy_2 <= new_vacancy_1
