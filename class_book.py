class Book:

    def __init__(self, list):
        self.__book_id = list[0]
        self.__name = list[1]
        self.__author = list[2]
        self.__year = list[3]
        self.__type = list[4]

    def get_book_id(self):
        return int(self.__book_id)

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_year(self):
        return int(self.__year)

    def get_type(self):
        return int(self.__type)

    def __str__(self):
        return f"{self.__book_id},{self.__name},{self.__author},{self.__year},{self.__type}"

