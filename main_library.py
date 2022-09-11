import function_library as func_l


def main():
    func_l.intro()
    choice = ''

    while choice != '13':
        print()
        print("\tMAIN MENU")
        print("\t1.	ADD NEW CUSTOMER")
        print("\t2.	ADD NEW BOOK")
        print("\t3.	LOAN BOOK")
        print("\t4.	RETURN BOOK")
        print("\t5.	DISPLAY ALL BOOKS")
        print("\t6.	DISPLAY ALL CUSTOMERS")
        print("\t7.	DISPLAY ALL LOANS")
        print("\t8.	DISPLAY LATE LOANS")
        print("\t9.	FIND BOOK BY NAME")
        print("\t10. FIND CUSTOMER BY NAME")
        print("\t11. REMOVE BOOK")
        print("\t12. REMOVER CUSTOMER")
        print("\t13. EXIT")
        print("\tSelect Your Option (1-13)")
        choice = input("\t")
        print()

        if choice == '1':
            print(func_l.add_new_customer())
            func_l.continue_work()
        elif choice == '2':
            print(func_l.add_new_book())
            func_l.continue_work()
        elif choice == '3':
            print(func_l.add_new_loan())
            func_l.continue_work()
        elif choice == '4':
            print(func_l.return_book())
            func_l.continue_work()
        elif choice == '5':
            func_l.show_all_books()
            func_l.continue_work()
        elif choice == '6':
            func_l.show_all_customers()
            func_l.continue_work()
        elif choice == '7':
            func_l.show_all_loans()
            func_l.continue_work()
        elif choice == '8':
            func_l.show_late_loans()
            func_l.continue_work()
        elif choice == '9':
            book_name = input("Please enter the book name: ")
            print(func_l.find_book_by_name(book_name))
            func_l.continue_work()
        elif choice == '10':
            customer_name = input("Please enter the customer's full name: ")
            print(func_l.find_customer_by_name(customer_name))
            func_l.continue_work()
        elif choice == '11':
            print(func_l.remove_book())
            func_l.continue_work()
        elif choice == '12':
            print(func_l.remove_customer())
            func_l.continue_work()
        elif choice == '13':
            print("Thanks for using library management system.")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
