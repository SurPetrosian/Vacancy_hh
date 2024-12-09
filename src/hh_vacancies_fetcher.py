import requests

from src.base_classes import BaseVacancyParser
from src.logger import logger_setup

api_logger = logger_setup()


class HeadHunterAPI(BaseVacancyParser):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    def fetch_vacancies(self, keyword: str, pages_amount: int) -> None:
        self.__params["text"] = keyword
        while self.__params["page"] != abs(pages_amount):
            api_logger.info(f"Parsing page number: {self.__params['page']}")
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                api_logger.info("Vacancies successfully added to list")
            self.__params["page"] += 1

    def squeeze(self) -> list:
        squeezed_info = []
        for vacancy in self.vacancies:
            try:
                if vacancy.get("salary").get("currency") == "RUR":
                    current_vacancy = dict()
                    current_vacancy["name"] = vacancy["name"]
                    current_vacancy["salary"] = vacancy.get("salary")
                    current_vacancy["url"] = vacancy["alternate_url"]
                    current_vacancy["requirement"] = vacancy["snippet"].get("requirement")
                    del current_vacancy["salary"]["gross"]
                    squeezed_info.append(current_vacancy)
            except AttributeError:
                continue
        return squeezed_info
