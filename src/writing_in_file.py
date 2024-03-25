from abc import ABC, abstractmethod
import json


class BaseWorkWithFile(ABC):
    @staticmethod
    @abstractmethod
    def write_json(a, b):
        pass


class WorkWithFile(BaseWorkWithFile):
    @staticmethod
    def write_json(info, file_name):
        """Записывает данные в файл json"""
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(info, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read_json(file_name, quantity_vacancion) -> list:
        """Считывает данные с json файла"""
        with open(file_name, encoding="utf-8") as file:
            return json.load(file)[:quantity_vacancion]

    @staticmethod
    def write_txt(txt_file, information):
        """Записывает информацию в текстовом формате в файл txt"""
        with open(txt_file, "w", encoding="utf-8") as file:
            file.write(information)
