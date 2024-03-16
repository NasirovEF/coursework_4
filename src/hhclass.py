from abc import ABC, abstractmethod
import requests


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
        return response.json().get("items")

    def writing_to_file(self):
        """Записывает полученные вакансии в файл json"""
        pass
