from datetime import date


class Warning:

    def __init__(self, id_person: int, warning_description: str, warning_date: date):
        self.__id_person = id_person
        self.__warning_description = warning_description
        self.__warning_date = warning_date

