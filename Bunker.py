import wikipediaapi
from pprint import pprint
import re
from collections import defaultdict
import csv
import openpyxl
import pandas as pd
import xlsxwriter


class Gender:
    Man = 1
    Woman = 2
    Helicopter = 3


ages = range(100)
age_groups = {
    0: ages[18:25],
    1: ages[25:50],
    -1: ages[50:70]
}


class Game:
    class BunkerCharacteristics:
        years_available = int()
        medical_office = bool()
        office_for_agriculture = bool()

    class Player:
        gender = int()
        age = int()

    class Context:
        pass


def main():
    pass


main()
