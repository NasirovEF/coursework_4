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
    if len(search.vacancies) == 0:
        print("К сожалению в указанном регионе вакансии не найдены. Выведены результаты по всем регионам")
        search.params['area'] = None
        search.load_vacancies()
    print(search)
    if len(search.vacancies) != 0:
        quantity_vacancion = int(input("Введите количество вакансий для вывода: "))
        with open("data/apivacancy.json", encoding="utf-8") as file:
            numb_vak = 0
            for v in json.load(file)[:quantity_vacancion]:
                vacancy = Vacancy(v)
                numb_vak += 1
                vacancy.writing_to_file(numb_vak, "data/vacancies.txt")
                print(vacancy)


if __name__ == '__main__':
    main()
