<h1 align="center">Проект 2. Поиск вакансий <a href="https://daniilshat.ru/" target="_blank"> </a> 
<h3 align="center"></h3>


<h4>Основной функционал</h4>

1. *base_classes* - модуль с определенными абстрактными классами. (Для синтаксического анализа API и файловых инструментов).
2. *file_tool* - класс **JSON-файлового инструмента**. При инициализации в качестве аргумента используется имя файла (параметр по умолчанию - "вакансия").
Позволяет прочитать json-файл, сохранить все или выбранные данные или удалить выбранные данные из файла.
3. *hh_vacancies_fetcher* - класс **HeadHunterAPI** - это класс, который работает только с HeadHunter API для получения вакансий по ключевому слову.
Дополнительный метод *squeeze* для фильтрации только ценной информации о вакансии.
4. *vacancy* - класс **Вакансия** для инициализации объекта вакансия. Поддерживает сравнение вакансий по зарплате.
При инициализации - если вакансии не хватает одного из атрибутов зарплаты - установите для него значение *0*. 
Позволяет добавить вакансию в общий список вакансий на уровне класса. 
5. *utils* - функции для работы с вакансиями - фильтрация, сортировка, ранжирование по зарплате, получение топ-листа и печать в удобном для чтения формате.


<h4>Как работает</h4>

Во время работы программа запросит у пользователя информацию, необходимую для поиска необходимых вакансий.
Пользователь может либо сохранить все вакансии в файле, либо выбрать только определенные вакансии, указав идентификационный номер вакансии.
Если вакансия была добавлена по ошибке, ее все еще можно удалить.


<h4>Тестирование и покрытие </h4>

Тесты для программы можно посмотреть в папке *tests*, тесты были реализованы на *pytest*, покрытие больше 90%
