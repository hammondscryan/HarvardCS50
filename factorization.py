def main():
    print(f"This is {__name__}.")
    intro()
    factors_list = create_factors_list()
    if factors_list is None:
        print("\n<<<Closing factorization program>>>")
    else:
        menu_choice = ''
        while menu_choice != 'q':
            menu_choice = main_menu_handler(factors_list)
            match menu_choice:
                case 'p':
                    print(f"\nThe factors of {factors_list[len(factors_list)-1]} are {factors_list}")
                case 'n':
                    factors_list = create_factors_list()
                    if factors_list is None:
                        menu_choice = 'q'
                        print("<<<Closing factorization program>>>")
                case 'q':
                    print("<<<Closing factorization program>>>")


def create_factors_list() -> list:
    factors_list = []
    num = input("\nEnter a positive integer to factorize (or q to quit): ").strip()
    while num != 'q':
        while not str.isnumeric(num) or int(num) < 1 or num == 'q':
            print("\nYou must enter a positive integer (i.e., whole number greater than 0).")
            num = input("Please re-enter your desired number (or q to quit): ").strip()
        if num != 'q':
            num = int(num)
            for _ in range(1, num+1):
                if num % _ == 0:
                    factors_list.append(_)
            return factors_list
        else:
            break
    return None



def intro():
    print("\n\n\nThis program provides the factors for a given positive integer.")
    print("The factors of a positive integer are those positive integers that evenly divide it (remainder of 0).")


def valid_menu_choice(choice) -> bool:
    if choice == 'p' or choice == 'n' or choice == 'q':
        return True
    else:
        return False


def main_menu_handler(factors_list: list) -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print(f"(p) Print the factors of {factors_list[len(factors_list)-1]}.")
        print("(n) Calculate the factors of a new positive integer.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice


if __name__ == "__main__":
    main()
