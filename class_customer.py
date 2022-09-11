
class Customer:

    def __init__(self, list):
        self.__cust_id = list[0]
        self.__name = list[1]
        self.__city = list[2]
        self.__age = list[3]

    def get_cust_id(self):
        return int(self.__cust_id)

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_age(self):
        return int(self.__age)

    def __str__(self):
        return f"{self.__cust_id},{self.__name},{self.__city},{self.__age}"


