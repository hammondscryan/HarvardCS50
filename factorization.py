def main():
    intro()
    factors_list = create_factors_list()
    while True:
        menu_choice = main_menu_handler(factors_list)
        match menu_choice:
            case 'p':
                print(f"\nThe factors of {factors_list[len(factors_list)-1]} are {factors_list}")
            case 'n':
                factors_list = create_factors_list()
            case 'q':
                exit("<<<Closing factorization program>>>")


def create_factors_list() -> list:
    factors_list = []
    while True:
        try:
            num = input("\nEnter a positive integer to factorize (or q to quit): ").strip()
            num = int(num)
        except ValueError:
            if num == 'q':
                exit("<<<Closing factorization program>>>")
            else:
                print("\nYou must enter a positive integer (i.e., whole number greater than 0).")
                pass
        else:
            if num<1:
                print("\nYou must enter a positive integer (i.e., whole number greater than 0).")
            else:
                break
    for _ in range(1, num+1):
        if num % _ == 0:
            factors_list.append(_)
    return factors_list


def intro():
    print("\n\n\nThis program provides the factors for a given positive integer.")
    print("The factors of a positive integer are those positive integers that evenly divide it (remainder of 0).")


def valid_menu_choice(choice) -> bool:
    match choice:
        case 'p' | 'n' | 'q':
            return True
        case _:
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
