import class_customer as c_c
import class_book as c_b
import class_loan as c_l
from datetime import date, timedelta, datetime


def add_new_book():
    """
    This function asks the user to enter book details:
        Book ID number
        Book Name
        Author
        Year Published
        Type(1/2/3)
    Checks if the given book is already on the list.
    If the book is not on the list, adds a new book to the file: books.txt
    """
    book_id = int(input("Please enter the ID number of the book: "))
    book = get_book_by_id(book_id)
    if book:
        return "This book is already on the list."
    book = c_b.Book([
        book_id,
        input("Please enter the name of the book: "),
        input("Please enter the Author of the book: "),
        int(input("Please enter the year of publication of the book: ")),
        int(input("Please enter book type(1/2/3): "))])
    with open('books.txt', 'a') as f:
        f.write(str(book) + '\n')
    return "New book was added."


def add_new_customer():
    """
    This function asks the user to enter customer details:
        Сustomer ID number
        Full name of the customer
        City of residence
        Age
    Checks if the given customer is already on the list.
    If the customer is not on the list, adds a new customer to the file: customers.txt
    """
    cust_id = int(input("Please enter the customer ID number: "))
    customer = get_customer_by_id(cust_id)
    if customer:
        return "This customer is already on the list."
    customer = c_c.Customer([
        cust_id,
        input("Please enter the customer full name: "),
        input("Please enter the city: "),
        int(input("Please enter the customer age: "))])
    with open('customers.txt', 'a') as f:
        f.write(str(customer) + '\n')
    return "New customer was added"


def add_new_loan():
    """
    This function asks the user to enter book details:
        Сustomer ID number
        Book Name
    Checks if this book is in the list of books, if not, returns to the main menu
    Checks if the given customer is already on the list of customers, if not,
    calls a function that adds a new customer and returns to the main menu
    The function checks if the book has been loaned to another customer,
    then returns the customer's data and return date.
    After all checks, the function adds a new loan to the file: loans.txt
    """
    loan_list = loan_reader()
    loan_day = date.today()
    id_cust = int(input("Please enter the customer ID number: "))
    book_name = input("Please enter the book name: ")
    book = find_book_by_name(book_name)
    if not book:
        return "Return to the Main menu and add the new book."
    customer = get_customer_by_id(id_cust)
    if not customer:
        print(add_new_customer())
        return "Return to the Main menu and add the new loan."
    return_day = day_of_return(book.get_type(), loan_day)
    if loan_list is not None:
        for loan in loan_list:
            ret_l_day = datetime.strptime(loan.get_return_date()[:-1], "%Y-%m-%d")
            if loan.get_book_id() == book.get_book_id():
                return (f"The book {book.get_name()} was loaned to the customer.\n"
                        f"The book will be available for loan after {loan.get_return_date()}")
            elif id_cust == loan.get_cust_id() and date.today() >= ret_l_day.date():
                return (f"This customer with ID number {loan.get_cust_id()}"
                       f"has not yet returned the loaned books on time.\n"
                        f"Please check which books have been loaned to this client")
    loan = c_l.Loan([id_cust, book.get_book_id(), loan_day, return_day])
    with open('loans.txt', 'a') as f:
        f.write(str(loan) + '\n')
    return "New loan was added."


def book_reader():
    """
    This function reads a file: book.txt, from this file returns book list
    :return: book list
    """
    book_l = []
    with open('books.txt', 'r') as f:
        reader = f.readlines()
    for i in range(1, len(reader)):
        if reader[i] != '\n':
            book_l.append(c_b.Book(reader[i].split(',')))
    return book_l


def continue_work():
    """
    This function outputs an empty string and asks the user to make an input
    """
    print()
    input("Please press 'Enter' to return to the Main Menu")


def customer_reader():
    """
    This function reads a file: customer.txt, from this file returns customer list
    :return: customer list
    """
    customer_l = []
    with open('customers.txt', 'r') as f:
        reader = f.readlines()
    for i in range(1, len(reader)):
        if reader[i] != '\n':
            customer_l.append(c_c.Customer(reader[i].split(',')))
    return customer_l


def day_of_return(book_type, loan_day):
    """
    This function takes the type of the book and the date the book was loaned
    and returns the day the book should be returned.
    :param book_type: book type
    :param loan_day: day when book was loaned
    :return: the date the book should be returned
    """
    return_day = 0
    if book_type == 1:
        return_day = loan_day + timedelta(10)
    elif book_type == 2:
        return_day = loan_day + timedelta(5)
    elif book_type == 3:
        return_day = loan_day + timedelta(2)
    return return_day


def find_book_by_name(book_name):
    """
    The function calls a function that reads the file: book.txt and gets the list of books.
    Searches the list of books for a book by the name it got and returns all of the book's data.
    If the book was not found in the list of books, the function returns False.
    :param book_name: name of the book
    :return: book or False
    """
    book_list = book_reader()
    for book in book_list:
        if book.get_name() == book_name:
            return book
    print("There is no that book on the book list.")
    return False


def find_customer_by_name(cust_name):
    """
    The function calls a function that reads the file: customers.txt and gets the list of customers.
    Searches the list of customers for a customer by the name it got
    and returns all the customer's data.
    If the customer was not found in the list of customers, the function returns False.
    :param cust_name: customer name
    :return: customer or False
    """
    customer_list = customer_reader()
    for customer in customer_list:
        if customer.get_name() == cust_name:
            return customer
    print("There is no such customer on the customer list.")
    return False


def get_customer_by_id(id_cust):
    """
    The function calls a function that reads the file: customers.txt and gets the list of customers.
    Searches the list of customers for a customer by the ID it got
    and returns all the customer's data.
    If the customer was not found in the list of customers, the function returns False.
    :param id_cust: customer ID
    :return: customer or False
    """
    customer_list = customer_reader()
    for customer in customer_list:
        if customer.get_cust_id() == id_cust:
            return customer
    print("There is no such customer on the customer list.")
    return False


def get_book_by_id(id_book):
    """
    The function calls a function that reads the file: book.txt and gets the list of books.
    Searches the list of books for a book by the book ID it got and returns all the book's data.
    If the book was not found in the list of books, the function returns False.
    :param id_book: book ID
    :return: book or False
    """
    book_list = book_reader()
    for book in book_list:
        if book.get_book_id() == id_book:
            return book
    print("There is no that book on the book list.")
    return False


def intro():
    """
    This function displays introductory text.
    """
    print("\t\t*************************")
    print("\t\tLIBRARY MANAGEMENT SYSTEM")
    print("\t\t*************************")


def loan_reader():
    """
    This function reads a file: loans.txt, from this returns file customer list
    :return: loan list
    """
    loan_l = []
    with open('loans.txt', 'r') as f:
        reader = f.readlines()
    for i in range(1, len(reader)):
        if reader[i] != '\n':
            loan_l.append(c_l.Loan(reader[i].split(',')))
    return loan_l


def remove_book():
    """
    This function calls a function that reads a file: book.txt and returns a list of books
    This function asks the user to enter book details:
        Book Name
    Checks if this book is on the list of books, if not, returns to the main menu.
    Opens the file: book.txt and overwrites the data by removing the selected book from it.
    """
    book_list = book_reader()
    book_name = input("Please enter the book name: ")
    book = find_book_by_name(book_name)
    if not book:
        return "There is no that book on the book list.\n"
    with open('books.txt', 'w') as book_file:
        book_file.write("BookID,Book name,Author,Year Published,Type\n")
        for book in book_list:
            if book.get_name() != book_name:
                book_file.write(str(book))
    return f"The book {book_name} was deleted from the list."


def remove_customer():
    """
    This function calls a function that reads a file: customers.txt and returns a list of customers
    This function asks the user to enter customer details:
        Customer ID
    Checks if this customer is on the list of customers, if not, returns to the main menu.
    Opens the file: customers.txt and overwrites the data by removing the selected customer from it.
    """
    customer_list = customer_reader()
    customer_id = int(input("Please enter the customer ID number: "))
    customer = get_customer_by_id(customer_id)
    if not customer:
        return "There is no such customer on the customer list."
    with open('customers.txt', 'w') as customer_file:
        customer_file.write("BookID,Book name,Author,Year Published,Type\n")
        for customer in customer_list:
            if customer.get_cust_id() != customer_id:
                customer_file.write(str(customer))
    return f"The customer {customer.get_name()} was deleted from the list."


def return_book():
    """
    This function calls a function that opens a file: loans.txt and returns a loan list.
    Asks the user to enter:
        customer ID
        book ID
    Opens the file: loans.txt and overwrites the data by removing the selected the loan from it.
    """
    loan_list = loan_reader()
    id_cust = int(input("Please enter the customer ID number: "))
    id_book = int(input("Please enter the book ID: "))
    customer = get_customer_by_id(id_cust)
    book = get_book_by_id(id_book)
    with open('loans.txt', 'w') as loan_file:
        loan_file.write("CustID,BookID,Loandate,Returndate\n")
        for loan in loan_list:
            if loan.get_cust_id() != id_cust and loan.get_book_id() != id_book:
                loan_file.write(str(loan))
    return f"The book {book.get_name()} was returned by {customer.get_name()}."


def show_all_books():
    """
    This function calls a function that reads a file: book.txt and returns a list of books
    and print all books
    """
    book_list = book_reader()
    for book in book_list:
        print(book, end='')


def show_all_customers():
    """
    This function calls a function that reads a file: customers.txt and returns a list of customers
    and print all customers
    """
    customer_list = customer_reader()
    for customer in customer_list:
        print(customer, end='')


def show_all_loans():
    """
    This function calls a function that reads a file: loans.txt and returns a list of loans
    and print all loans
    """
    loan_list = loan_reader()
    for loan in loan_list:
        print(loan, end='')


def show_late_loans():
    """
    This function calls a function that reads a file: loans.txt and returns a list of loans
    Checks if the date the book should have been returned is earlier than today returns the book.
    """
    loan_list = loan_reader()
    for loan in loan_list:
        loan_day = datetime.strptime(loan.get_return_date()[:-1], "%Y-%m-%d")
        if date.today() > loan_day.date():
            book = get_book_by_id(loan.get_book_id())
            customer = get_customer_by_id(loan.get_cust_id())
            timedelta = date.today() - loan_day.date()
            print(loan,
                f"The book {book.get_name()} was loaned to the customer {customer.get_name()}\n"
                f"The book was not returned on time to the library"
                f" and the return was overdue by {timedelta.days} days.")
