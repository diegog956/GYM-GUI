from datetime import date

class Gym_Routine:

    def __init__(self, id_person: int, routine_description: str, routine_date: date):
        self.__id_person = id_person
        self.__routine_description = routine_description
        self.__routine_date = routine_date

