# User facing code
import database


# Prompt: show the user everytime
MENU_PROMPT = """-- Coffee Bean App --

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection:
"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = "start"

    while user_input != 5:
        user_input = int(input(MENU_PROMPT))

        if user_input == 1:
            name = str(input("Enter the name of the bean: "))
            method = str(input("Enter how you've prepared the bean: "))
            rating = int(input("Enter your rating score (0-100): "))
            database.add_bean(connection, name, method, rating)
        elif user_input == 2:
            beans = database.get_all_beans(connection)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == 3:
            name = str(input("Enter the name of the bean to find: "))
            beans = database.get_beans_by_name(connection, name)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == 4:
            name = str(input("Enter the name of the bean to find: "))
            best_method = database.get_best_preparation_for_bean(connection, name)
            print(f"The best preparation method for the bean {name} is {best_method[2]}")
        elif user_input == 5:
            print("Will exit program now...")
        else:
            print("Invalid user input. Please try again")


menu()
