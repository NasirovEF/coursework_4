from abc import ABC, abstractmethod
import requests
import json


class ApiClass(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancy(self):
        pass


class HeadHunterAPI(ABC):
    """Класс для работы с платформой hh.ru"""

    def __init__(self) -> None:
        """Конструктор для класса"""
        self.url = "https://api.hh.ru/vacancies"

    def get_information(self) -> dict:
        """Метод для подключения через API к HH и получение вакансий"""
        response = requests.get(self.url)
        return response.json() #.get("items")

    def writing_to_file(self):
        """Записывает полученные вакансии в файл json"""
        with open("../data/apivacancy.json", "w", encoding="utf-8") as file:
            json.dump(self.get_information(), file, indent=4, ensure_ascii=False)

    def __str__(self):
        return f'Найдено {self.get_information.get("found")} вакансий'
