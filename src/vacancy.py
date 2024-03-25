class Vacancy:

    def __init__(self, vacancy):
        """Конструктор для класса"""
        self.name = vacancy.get('name')
        self.url = vacancy.get('alternate_url')
        if vacancy.get('address') is None:
            self.address = "не указан"
        else:
            self.address = vacancy.get('address')['raw']
        if vacancy.get('snippet')['requirement'] is None:
            self.requirement = "не указаны"
        else:
            self.requirement = vacancy.get('snippet')['requirement']
        self.responsibility = vacancy.get('snippet')['responsibility']
        if vacancy.get('salary')['from'] is None:
            self.__salary_from = 0
        else:
            self.__salary_from = vacancy.get('salary')['from']
        self.__salary_to = vacancy.get('salary')['to']

    @property
    def salary_from(self):
        """Геттер для нижней границы зарплаты"""
        return self.__salary_from

    @property
    def salary_to(self):
        """Геттер для верхней границы зарплаты"""
        return self.__salary_to

    def __str__(self):
        return (f'{self.name}\nЗарплата: {self.__salary_from} - {self.__salary_to}\n'
                f'Адрес: {self.address}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}\n'
                f'Ссылка на вакансию {self.url}\n')
