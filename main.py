from src.hhclass import HeadHunterAPI


def main():
    """Функция запускающая программу и взаимодействующая с пользователем"""
    search = HeadHunterAPI()
    search.get_name_vakancy(str(input("Введите название профессии: ")))
    search.get_salary(int(input("Введите уровень желаемой зарплаты: ")))
    search.get_region()
    search.load_vacancies()
    search.write_json(search.vacancies,"data/apivacancy.json")
    if len(search.vacancies) == 0:
        print("К сожалению в указанном регионе вакансии не найдены. Выведены результаты по всем регионам")
        search.params['area'] = None
        search.load_vacancies()
    print(search)
    if len(search.vacancies) != 0:
        quantity_vacancion = int(input("Введите количество вакансий для вывода: "))
        vak_list = search.read_json("data/apivacancy.json", quantity_vacancion)
        vak_str = search.get_str_vak(vak_list)
        search.write_txt("data/vacancies.txt", vak_str)
        print(vak_str)


if __name__ == '__main__':
    main()
