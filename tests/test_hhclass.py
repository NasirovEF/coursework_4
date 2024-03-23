import pytest
from src.hhclass import HeadHunterAPI


@pytest.fixture
def headhant():
    hh = HeadHunterAPI()
    return hh


def test_get_salary(headhant):
    headhant.get_salary(50000)
    assert headhant.params['salary'] == 50000


def test_get_name_vakancy(headhant):
    headhant.get_name_vakancy("Python")
    assert headhant.params['text'] == "Python"
