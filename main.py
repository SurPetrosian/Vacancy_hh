import json
import re
from time import sleep

from src.file_tool import JsonFileTool
from src.hh_vacancies_fetcher import HeadHunterAPI
from src.logger import logger_setup
from src.utils import (
    filter_by_description,
    get_top_n_vacancies,
    print_vacancies,
    range_vacancies_by_salary,
    sort_vacancies,
)
from src.vacancy import Vacancy

main_logger = logger_setup()


def user_setup() -> dict:
    search_query = input("Пожалуйста, введите ключевое слово для поиска вакансии: \n")
    try:
        page_numbers = abs(
            int(input("Пожалуйста, введите количество страниц для поиска (каждая страница содержит 100 вакансий): \n"))
        )
        top_n = abs(int(input("Пожалуйста, укажите количество N лучших вакансий, которые вы хотите получить: \n")))
    except ValueError:
        print("Неверные данные. Значения установлены по умолчанию. Количество страниц: 20, N самых популярных вакансий: 5\n")
        page_numbers = 20
        top_n = 5
    filter_words = input(
        """Пожалуйста, введите ключевые слова для фильтрации по описанию вакансии (используйте пробел для разделения)
         или нажмите Enter, чтобы пропустить этот шаг: \n"""
    ).split()
    salary_range = input(
        "Пожалуйста, введите диапазон заработной платы в соответствии с форматом (1000-2000). Для одного значения "
        "введите в формате (2000-2000): \n"
    )
    if len(re.split("[,;-]", salary_range)) != 2 or not all(x.isdigit() for x in re.split("[,;-]", salary_range)):
        print("Неверный формат. По умолчанию задан диапазон зарплат: 0-1000000\n")
        sleep(2)
        salary_range = "0-1000000"

    settings_info = {
        "search_query": search_query,
        "page_numbers": page_numbers,
        "top_n": top_n,
        "filter_words": filter_words,
        "salary_range": salary_range,
    }
    return settings_info


def working_with_vacancies(settings: dict) -> list:
    head_hunter_fetcher = HeadHunterAPI()
    head_hunter_fetcher.fetch_vacancies(settings["search_query"], settings["page_numbers"])
    formatted_vacancies = head_hunter_fetcher.squeeze()
    for vacancy in formatted_vacancies:
        one_vacancy = Vacancy(vacancy)
        Vacancy.cast_vacancies_to_list(one_vacancy)
    if settings["filter_words"]:
        filtered_vacancies = filter_by_description(Vacancy.vacancies_list, settings["filter_words"])
    else:
        filtered_vacancies = Vacancy.vacancies_list
    ranged_vacancies = range_vacancies_by_salary(filtered_vacancies, settings["salary_range"])
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n_vacancies = get_top_n_vacancies(sorted_vacancies, settings["top_n"])
    return top_n_vacancies


def work_with_file(vacancies: list) -> None:
    filename_choice = input("Пожалуйста, введите имя для json-файла (или оставьте пустым имя по умолчанию).: \n")
    if filename_choice:
        json_handler = JsonFileTool(filename_choice)
    else:
        json_handler = JsonFileTool()
    method_choice = input(
        "Если вы хотите сохранить все вакансии, введите 'все'. Если вы хотите выбрать конкретные вакансии, "
        "введите 'выбрать': \n"
    )
    if method_choice.lower() == "all":
        json_handler.save_all_to_file(vacancies)

    elif method_choice.lower() == "choose":
        user_choice = input(
            "Пожалуйста, выберите порядковые номера вакансий (разделенные пробелом или запятой), которые вы хотели бы "
            "сохранить: \n"
        )
        index_choice = re.split("[,; ]", user_choice)
        index_numbers = list(map(int, index_choice))
        json_handler.save_chosen_to_file(vacancies, index_numbers)

    else:
        print("Неверный ввод. Все вакансии будут сохранены.\n")
        json_handler.save_all_to_file(vacancies)

    delete_choice = input("Вы хотите удалить некоторые вакансии из файла? [да/нет]: \n")
    if delete_choice.lower() in ["да"]:
        with open(json_handler.path, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        for index, vacancy in enumerate(vacancies, 1):
            print(f"Vacancy #{index}\n {vacancy}")
        user_choice = input(
            "\nПожалуйста, выберите порядковые номера вакансий (разделенные пробелом или запятой), которые вы хотели бы удалить: \n"
        )
        index_choice = re.split("[,; ]", user_choice)
        index_numbers = list(map(int, index_choice))
        json_handler.remove_from_file(index_numbers)
    else:
        print("Закончена работа с файлом\n")


def main_interaction() -> None:
    running_app = True
    while running_app:
        user_settings = user_setup()
        print("Настроен инструмент поиска. Пожалуйста подождите\n")
        sleep(2)

        user_vacancies = working_with_vacancies(user_settings)
        print("Вывод вакансий на консоль\n")
        sleep(2)

        print_vacancies(user_vacancies)
        file_choice = input("Вы хотите сохранить вакансии в файле? [да/нет]: \n")
        if file_choice.lower() in ["да"]:
            work_with_file(user_vacancies)
        running_app = False

    print("Спасибо")
    input("\n\n\nНажмите Enter для выхода.")


if __name__ == "__main__":
    main_interaction()
