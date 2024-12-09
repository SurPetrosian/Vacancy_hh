class Vacancy:

    vacancy_info: dict

    vacancies_list = []

    __slots__ = ("__name", "__salary", "__url", "__requirement", "__vacancy_info")

    def __init__(self, vacancy_info):
        self.__name = vacancy_info.get("name")
        self.__salary = vacancy_info.get("salary")
        self.__url = vacancy_info.get("url")
        self.__requirement = vacancy_info.get("requirement")
        self.__validate_data()
        self.__vacancy_info = vacancy_info

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def requirement(self):
        return self.__requirement

    @property
    def vacancy_info(self):
        return self.__vacancy_info

    @property
    def salary(self):
        return self.__salary

    def __len__(self):
        return len(self.vacancies_list)

    def __gt__(self, other):
        if type(self) is type(other):
            return self.get_max_salary() > other.get_max_salary()

    def __lt__(self, other):
        if type(self) is type(other):
            return self.get_max_salary() < other.get_max_salary()

    def __ge__(self, other):
        if type(self) is type(other):
            return self.get_max_salary() >= other.get_max_salary()

    def __le__(self, other):
        if type(self) is type(other):
            return self.get_max_salary() <= other.get_max_salary()

    def __validate_data(self):
        if self.__salary["to"] is None:
            self.__salary["to"] = 0
        if self.__salary["from"] is None:
            self.__salary["from"] = 0
        if self.__requirement is None:
            self.__requirement = "No information"

    def get_max_salary(self):
        return max(self.salary["from"], self.salary["to"])

    @classmethod
    def cast_vacancies_to_list(cls, vacancy):
        cls.vacancies_list.append(vacancy)
