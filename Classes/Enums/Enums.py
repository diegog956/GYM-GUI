from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class BloodType(Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"


class Member_Type(Enum):
    MEMBER = 1
    INSTRUCTOR = 2
    MAINTENANCE = 3
    CLEANING = 4


class Type_Groupclass(Enum):
    WeightRoom = 0
    CrossFit = 1
    Spinning = 2
    Box = 3
