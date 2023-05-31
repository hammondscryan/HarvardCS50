def main():
    print_intro()
    fib_list = create_fib_list()
    while True:
        menu_choice = main_menu_handler(fib_list)
        match menu_choice:
            case 'p':
                print(f"\n{fib_list}")
            case '<':
                print(f"\n{less_than_option(fib_list)}")
            case 'o':
                print(f"\n{odd_option(fib_list)}")
            case 'e':
                print(f"\n{even_option(fib_list)}")
            case 'n':
                fib_list = create_fib_list()
            case 'q':
                exit("<<<Closing Fibonacci program>>>")


def print_intro():
    print("\n\n\nThis program generates the first n terms of the Fibonacci sequence!")
    print("Remember that the first two terms in the sequence will always be 1.")
    print("So, n should be greater than or equal to 2.")
    print("Enter q to quit.")


def create_fib_list():
    fib_list = [1, 1]
    while True:
        try:
            num_terms = input("How many terms in the sequence would you like to generate (or q to quit)?").strip()
            num_terms = int(num_terms)
        except ValueError:
            if num_terms == 'q':
                exit("<<<Closing Fibonacci program>>>")
            else:
                print("\nThe quantity of desired terms must be 2 or more.")
                pass
        else:
            if num_terms < 2:
                print("\nThe quantity of desired terms must be 2 or more.")
            else:
                break
    for _ in range(2, num_terms):
        fib_list.append(fib_list[_ - 2] + fib_list[_ - 1])
    return fib_list


def valid_menu_choice(choice) -> bool:
    match choice:
        case 'p' | '<' | 'o' | 'e' | 'n' | 'q':
            return True
        case _:
            return False


def main_menu_handler(fib_list: list) -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print(f"(p) Print your sequence of {len(fib_list)} numbers.")
        print("(<) Print all numbers less than or equal to a given number.")
        print("(o) Print out all odd numbers in your list.")
        print("(e) Print out all even numbers in your list.")
        print("(n) Generate a new list.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice


def less_than_option(fib_list: list) -> list:
    while True:
        try:
            upper_b = input("\nEnter your desired upper bound: ").strip()
            upper_b = int(upper_b)
        except ValueError:
            print(f"\nThe max value must be a whole number between 1 and {fib_list[len(fib_list) - 1]}, inclusive.")
            pass
        else:
            if int(upper_b) > fib_list[len(fib_list) - 1] or int(upper_b) < 1:
                print(f"\nThe max value must be a whole number between 1 and {fib_list[len(fib_list) - 1]}, inclusive.")
            else:
                break
    bounded_list = []
    for _ in fib_list:
        if _ <= upper_b:
            bounded_list.append(_)
    return bounded_list


def odd_option(fib_list: list) -> list:
    odd_list = []
    for _ in fib_list:
        if _ % 2 == 1:
            odd_list.append(_)
    return odd_list


def even_option(fib_list: list) -> list:
    even_list = []
    for _ in fib_list:
        if _ % 2 == 0:
            even_list.append(_)
    return even_list


if __name__ == "__main__":
    main()
    