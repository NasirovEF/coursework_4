import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_fixt_1():
    v = {'name': 'охранник', 'alternate_url': "skypro.ru", 'address': {'raw': 'Moscow'},
         'snippet': {'requirement': 'требования', 'responsibility': 'обязанности'},
         'salary': {'from': 50000, 'to': 100000}}
    return Vacancy(v)


@pytest.fixture
def vacancy_fixt_2():
    v = {'name': 'охранник', 'alternate_url': "skypro.ru", 'address': None,
         'snippet': {'requirement': None, 'responsibility': 'обязанности'},
         'salary': {'from': 0, 'to': 100000}}
    return Vacancy(v)


def test_init_vacancy_1(vacancy_fixt_1):
    assert vacancy_fixt_1.name == 'охранник'
    assert vacancy_fixt_1.url == 'skypro.ru'
    assert vacancy_fixt_1.address == 'Moscow'
    assert vacancy_fixt_1.requirement == 'требования'
    assert vacancy_fixt_1.responsibility == 'обязанности'
    assert vacancy_fixt_1.salary_from == 50000
    assert vacancy_fixt_1.salary_to == 100000


def test_init_vacancy_2(vacancy_fixt_2):
    assert vacancy_fixt_2.address == 'не указан'
    assert vacancy_fixt_2.requirement == 'не указаны'
    assert vacancy_fixt_2.salary_from == 0


def test_str_vacancy(vacancy_fixt_1):
    assert str(vacancy_fixt_1) == ("охранник\nЗарплата: 50000 - 100000\n"
                                   "Адрес: Moscow\nТребования: требования\nОбязанности: обязанности\n"
                                   "Ссылка на вакансию skypro.ru\n")
