import json

from src.base_classes import BaseFileTool


class JsonFileTool(BaseFileTool):


    filename: str

    def __init__(self, filename="vacancies"):
        self.__filename = filename
        self.path = f"data/{self.__filename}.json"

    @property
    def filename(self):
        return self.__filename

    def get_data_from_file(self) -> list | dict:
        with open(self.path, "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
            return content

    def save_all_to_file(self, vacancy_list: list) -> None:
        ready_to_save = []
        for vacancy in vacancy_list:
            ready_to_save.append(vacancy.vacancy_info)
        with open(self.path, "w", encoding="utf-8") as json_file:
            json.dump(ready_to_save, json_file, indent=4, ensure_ascii=False)

    def save_chosen_to_file(self, vacancy_list: list, index_numbers: list) -> None:
        ready_to_save = []
        for number in sorted(index_numbers, reverse=True):
            ready_to_save.append(vacancy_list[number - 1].vacancy_info)
        with open(self.path, "w", encoding="utf-8") as json_file:
            json.dump(ready_to_save, json_file, indent=4, ensure_ascii=False)

    def remove_from_file(self, index_numbers: list) -> None:
        with open(self.path, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
            for number in sorted(index_numbers, reverse=True):
                try:
                    vacancies.pop(number - 1)
                except IndexError:
                    continue
        with open(self.path, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)
