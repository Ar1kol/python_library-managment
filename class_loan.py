from datetime import date, timedelta, datetime


class Loan:

    def __init__(self, list):
        self.__cust_id = list[0]
        self.__book_id = list[1]
        self.__loan_date = list[2]
        self.__return_date = list[3]

    def get_cust_id(self):
        return int(self.__cust_id)

    def get_book_id(self):
        return int(self.__book_id)

    def get_loan_date(self):
        return self.__loan_date

    def get_return_date(self):
        return self.__return_date

    def __str__(self):
        return f"{self.__cust_id},{self.__book_id},{self.__loan_date},{self.__return_date}"
