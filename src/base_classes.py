from abc import ABC, abstractmethod


class BaseVacancyParser(ABC):
    """Abstract class for vacancy parsers"""

    @abstractmethod
    def fetch_vacancies(self, keyword, pages_amount):
        pass

    @abstractmethod
    def squeeze(self):
        pass


class BaseFileTool(ABC):
    """Abstract class for working with files"""

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def save_all_to_file(self, vacancy_list):
        pass

    @abstractmethod
    def save_chosen_to_file(self, vacancy_list, index_numbers):
        pass

    @abstractmethod
    def remove_from_file(self, index_numbers):
        pass
