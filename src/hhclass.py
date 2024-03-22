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
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100,
                       'only_with_salary': True}
        self.vacancies = []

    def get_salary(self, salary) -> None:
        """Метод для внесения в параметры поиска зарплаты"""
        self.params['salary'] = salary

    def load_vacancies(self, keyword):
        """Метод для подключения через API к HH и получение вакансий"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def writing_to_file(self):
        """Записывает полученные вакансии в файл json"""
        with open("../data/apivacancy.json", "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)

    def get_region(self):
        """Метод, позволяющий выбрать регион поиска вакансий"""
        area_url = "https://api.hh.ru/suggests/areas"
        city = str(input("Введите регион поиска "))
        area_params = {'text': city}
        area_response = requests.get(area_url, params=area_params)
        if len(area_response.json().get('items')) == 0:
            print("К сожалению ничего не найдено. Поиск будет осуществлен по всем регионам")
            self.params['area'] = None
        else:
            for item in area_response.json().get('items'):
                print(f'{item['text']} - {item['id']}')
            user_input = input("Введите id выбранного региона ")
            self.params['area'] = int(user_input)

    def __str__(self):
        return f'Найдено {len(self.vacancies)} вакансий'


exp2 = HeadHunterAPI()
keyword1 = "python"
exp2.get_region()
exp2.get_salary(100000)
exp2.load_vacancies(keyword1)
exp2.writing_to_file()
print(exp2)

