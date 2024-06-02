from datetime import date

from Classes.Entities.Person import Person
from Classes.Enums.Enums import *


class Employee(Person):

    def __init__(self, id_person: int, id_gym: int, first_name: str, last_name: str, birthdate: date, phone: str,
                 address: str, gender: Gender, blood_type: BloodType, emergency_contact: str,
                 employee_type: Employee_Type):
        super().__init__(id_person, id_gym, first_name, last_name, birthdate, phone, address, gender, blood_type,
                         emergency_contact)
        self._employee_type = employee_type

    @property
    def _employee_type(self):
        return self._employee_type

