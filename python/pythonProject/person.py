import random
import datetime

class Person:
    name = ''
    gender = ''
    _DOB = ''   #private variable
    _PAN_no= '' #private variable
    balance = 0
    PIN = 0000
    Acc_No = ''
    age = 0

    def __init__(self):
        self.name = self.name()
        self.gender = self.gender()
        self._DOB  , self.age = self.dob()
        self._PAN_no = random.randint(10000000 , 99999999)
        self.balance = 0.0
        self.PIN = self.pin()
        self.Acc_No = random.randint(1000000000 , 9999999999)

    def name(self):
        name = input('Enter your name : ')
        return name
    def gender(self):
        while True:
            gen = input('Enter M for Male, F for Female, or O for others: ').upper()
            if gen in ('M', 'F', 'O'):
                return gen
            else:
                print('Invalid input. Please enter M, F, or O.')
    def dob(self):
        bdate = input("Type your Date of birth (e.g., 10/11/2024): ")
        day, month, year = map(int, bdate.split('/'))
        birth_date = datetime.date(year, month, day)
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        return birth_date, age # here age is also calculated and is passed with bod
    def pin(self):
        while True:
            pin = input("Enter the four-digit PIN for your Account: ")
            if pin.isdigit() and len(pin) == 4:
                return pin
            else:
                print('Invalid PIN. Please enter a four-digit number.')


