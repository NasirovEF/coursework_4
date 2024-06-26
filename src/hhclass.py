from abc import ABC, abstractmethod
import requests
from src.writing_in_file import WorkWithFile
from src.vacancy import Vacancy


class ApiClass(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self):
        pass


class HeadHunterAPI(ApiClass, WorkWithFile):
    """Класс для работы с платформой hh.ru"""

    def __init__(self) -> None:
        """Конструктор для класса"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100,
                       'only_with_salary': True}
        self.vacancies = []

    def get_salary(self, salary) -> None:
        """Метод для внесения в параметры поиска зарплаты"""
        self.params['salary'] = salary

    def get_name_vakancy(self, keyword):
        """Метод для внесения в параметры поиска названия вакансии"""
        self.params['text'] = keyword

    def load_vacancies(self):
        """Метод для подключения через API к HH и получение вакансий"""
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    # метод не доработал пока что
    # def sort_vakancy(self):
    #     """Метод для сортировки вакансий по зарплате"""
    #     sorted(self.vacancies, key=lambda vacancy: vacancy.get('salary')['from'])

    def get_region(self):
        """Метод, позволяющий выбрать регион поиска вакансий"""
        area_url = "https://api.hh.ru/suggests/areas"
        city = str(input("Введите регион поиска: "))
        area_params = {'text': city}
        area_response = requests.get(area_url, params=area_params)
        if len(area_response.json().get('items')) == 0:
            print("К сожалению ничего не найдено. Поиск будет осуществлен по всем регионам")
            self.params['area'] = None
        else:
            for item in area_response.json().get('items'):
                print(f'{item['text']} - id {item['id']}')
            user_input = input("Введите id выбранного региона ")
            self.params['area'] = int(user_input)

    @staticmethod
    def get_str_vak(vacancies):
        """Метод для создания объектов класса Vacancy"""
        vak_str = ""
        numb_vak = 0
        for vakancy in vacancies:
            inst_vacancy = Vacancy(vakancy)
            numb_vak += 1
            vak_str += f'\n№{numb_vak} {str(inst_vacancy)}'

        return vak_str

    def __str__(self):
        return f'По запросу "{self.params['text']}" найдено {len(self.vacancies)} вакансий'
