from datetime import *
from Classes.Enums.Enums import Gender, BloodType


class Person:

    def __init__(self, id_person: int, id_gym: int, first_name: str, last_name: str,
                 birthdate: date, phone: str, address: str,  email:str,
                 gender: Gender, blood_type: BloodType, emergency_contact: str):
        self._id_person = id_person
        self._id_gym = id_gym
        self._first_name = first_name
        self._last_name = last_name
        self._birthdate = birthdate
        self._phone = phone
        self._address = address
        self._email = email
        self._gender = gender
        self._blood_type = blood_type
        self._emergency_contact = emergency_contact

    @property
    def _id_person(self) -> int:
        return self._id_person

    @property
    def _id_gym(self) -> int:
        return self._id_gym

    @property
    def _first_name(self) -> str:
        return self._first_name

    @property
    def _last_name(self) -> str:
        return self._last_name

    @property
    def _birthdate(self) -> date:
        return self._birthdate

    @property
    def _phone(self) -> str:
        return self._phone

    @property
    def _address(self) -> str:
        return self._address

    @_address.setter
    def _address(self, value: str):
        self._address = value

    @property
    def _email(self, value:str):
        return self._email

    @property
    def _gender(self) -> Gender:
        return self._gender

    @property
    def _blood_type(self) -> BloodType:
        return self._blood_type

    @property
    def _emergency_contact(self) -> str:
        return self._emergency_contact

    @_emergency_contact.setter
    def _emergency_contact(self, value: int):
        self._emergency_contact = value
