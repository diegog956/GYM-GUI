from datetime import date

from Classes.Entities.Person import Person
from Classes.Enums.Enums import Gender, BloodType


class Member(Person):
    def __init__(self, id_person: int, id_gym: int, first_name: str, last_name: str,
                 birthdate: date, phone: str, address: str,
                 gender: Gender, bloodType: BloodType, emergency_contact: str,
                 debt_amount: float, due_date: date):
        super().__init__(id_person, id_gym, first_name, last_name, birthdate, phone, address, gender, bloodType,
                         emergency_contact)
        self._debt_amount = debt_amount
        self._due_date = due_date

    @property
    def __debt_amount(self) -> float:
        return self._debt_amount

    @__debt_amount.setter
    def __debt_amount(self, value: float):
        self._debt_amount = value

    @property
    def __due_date(self) -> date:
        return self._due_date
