from abc import ABC, abstractmethod
import requests
import json


class ApiClass(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def et_vacancy(self):
        pass


class HeadHunterAPI(ABC):
    """Класс для работы с платформой hh.ru"""

    def __init__(self, url) -> None:
        """Конструктор для класса"""
        self.url = url

    def get_vacancy(self) -> dict:
        """Метод для подключения через API к HH и получение вакансий"""
        response = requests.get(self.url)
        return response.json() #.get("items")

    def writing_to_file(self):
        """Записывает полученные вакансии в файл json"""
        with open("../data/apivacancy.json", "w", encoding="utf-8") as file:
            json.dump(self.get_vacancy(), file, ensure_ascii=False)

    def __str__(self):
        return f'Найдено {self.get_vacancy().get("found")} вакансий'




# url = "https://api.hh.ru/vacancies"
#
# vacancy = HeadHunterAPI(url)
# vacancy.writing_to_file()
# print(vacancy)
