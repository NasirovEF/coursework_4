import json
from src.hhclass import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    """Функция запускающая программу и взаимодействующая с пользователем"""
    search = HeadHunterAPI()
    search.get_name_vakancy(str(input("Введите название профессии: ")))
    search.get_salary(int(input("Введите уровень желаемой зарплаты: ")))
    search.get_region()
    search.load_vacancies()
    search.writing_to_file("data/apivacancy.json")
    print(search)
    quantity_vacancion = int(input("Введите количество вакансий для вывода: "))
    with open("data/apivacancy.json", encoding="utf-8") as file:
        for v in json.load(file)[:quantity_vacancion]:
            vacancy = Vacancy(v)
            vacancy.writing_to_file("data/vacancies.txt")
            print(vacancy)


if __name__ == '__main__':
    main()
