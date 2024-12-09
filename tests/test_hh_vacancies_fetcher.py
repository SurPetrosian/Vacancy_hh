from unittest.mock import Mock, patch

from src.hh_vacancies_fetcher import HeadHunterAPI


def test_hhapi_init():
    hh_fetcher = HeadHunterAPI()
    assert hh_fetcher.url == "https://api.hh.ru/vacancies"
    assert hh_fetcher.params == {"text": "", "page": 0, "per_page": 100}
    assert hh_fetcher.headers == {"User-Agent": "HH-User-Agent"}
    assert hh_fetcher.vacancies == []


def test_fetch_vacancies():
    hh_fetcher = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": ["test"]}

    with patch("requests.get", return_value=mock_response):
        hh_fetcher.fetch_vacancies("python", 20)
        assert len(hh_fetcher.vacancies) == 20


def test_fetch_vacancies_failed():
    hh_fetcher = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 404

    with patch("requests.get", return_value=mock_response):
        hh_fetcher.fetch_vacancies("python", 5)
        assert hh_fetcher.vacancies == []


def test_squeeze(vacancy_full_info):
    hh_fetcher = HeadHunterAPI()
    hh_fetcher.vacancies.append(vacancy_full_info)
    assert hh_fetcher.squeeze() == [
        {
            "name": "Java Developer",
            "salary": {"from": 50000, "to": 80000, "currency": "RUR"},
            "url": "https://hh.ru/vacancy/108174610",
            "requirement": "At least 2 years of practical experience with <highlighttext>Java</highlighttext> development. A strong understanding of Spring, Hibernate and OOP principles and...",
        }
    ]


def test_squeeze_attribute_error():
    test_vacancy = {"name": "test", "salary": "test"}
    hh_fetcher = HeadHunterAPI()
    hh_fetcher.vacancies.append(test_vacancy)
    assert hh_fetcher.squeeze() == []
