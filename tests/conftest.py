import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return {
        "name": "Python developer",
        "salary": {"from": 100, "to": 300, "currency": "RUR"},
        "url": "test_url",
        "requirement": "SQL",
    }


@pytest.fixture
def vacancy_2():
    return {
        "name": "Java developer",
        "salary": {"from": None, "to": 300, "currency": "RUR"},
        "url": "test_url",
        "requirement": "Java",
    }


@pytest.fixture
def vacancy_3():
    return {
        "name": "DevOps",
        "salary": {"from": 100, "to": None, "currency": "RUR"},
        "url": "test_url",
        "requirement": "Management skills",
    }


@pytest.fixture
def vacancy_4():
    return {
        "name": "Senior Python developer",
        "salary": {"from": 400, "to": 600, "currency": "RUR"},
        "url": "test_url",
        "requirement": "SQL",
    }


@pytest.fixture
def vacancy_5():
    return {
        "name": "C++ developer",
        "salary": {"from": 300, "to": 400, "currency": "RUR"},
        "url": "test_url",
        "requirement": None,
    }


@pytest.fixture
def vacancies_list(vacancy_1, vacancy_2, vacancy_3, vacancy_4, vacancy_5):
    return [Vacancy(vacancy_1), Vacancy(vacancy_2), Vacancy(vacancy_3), Vacancy(vacancy_4), Vacancy(vacancy_5)]


@pytest.fixture
def vacancy_full_info():
    return {
        "id": "108174610",
        "premium": False,
        "name": "Java Developer",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "2759", "name": "Ташкент", "url": "https://api.hh.ru/areas/2759"},
        "salary": {"from": 50000, "to": 80000, "currency": "RUR", "gross": False},
        "type": {"id": "open", "name": "Открытая"},
        "address": {
            "city": "Ташкент",
            "street": "улица Тараса Шевченко",
            "building": "21А",
            "lat": 41.297617,
            "lng": 69.280752,
            "description": None,
            "raw": "Ташкент, улица Тараса Шевченко, 21А",
            "metro": None,
            "metro_stations": [],
            "id": "13753929",
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-10-04T11:45:28+0300",
        "created_at": "2024-10-04T11:45:28+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108174610",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/108174610?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/108174610",
        "relations": [],
        "employer": {
            "id": "10051975",
            "name": "VENTION",
            "url": "https://api.hh.ru/employers/10051975",
            "alternate_url": "https://hh.ru/employer/10051975",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/1130920.png",
                "90": "https://img.hhcdn.ru/employer-logo/6144269.png",
                "240": "https://img.hhcdn.ru/employer-logo/6144270.png",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10051975",
            "accredited_it_employer": False,
            "trusted": True,
        },
        "snippet": {
            "requirement": "At least 2 years of practical experience with <highlighttext>Java</highlighttext> development. A strong understanding of Spring, Hibernate and OOP principles and...",
            "responsibility": "Developing our solution set with a commitment to deliver high-quality code to production. Participating in the full cycle of...",
        },
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
