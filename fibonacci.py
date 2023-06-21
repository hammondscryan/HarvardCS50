def main():
    print_intro()
    fib_list = create_fib_list()
    while True:
        menu_choice = main_menu_handler(fib_list)
        match menu_choice:
            case 'p':
                print(f"\n{fib_list}")
            case 'u':
                u_b_list = upper_bounded_list(fib_list)
                if not u_b_list:
                    print("The given upper bound is less than the terms in your sequence.")
                else:
                    print(f"\n{u_b_list}")
            case 'l':
                l_b_list = lower_bounded_list(fib_list)
                if not l_b_list:
                    print("The given lower bound is greater than the terms in your sequence.")
                else:
                    print(f"\n{l_b_list}")
            case 'o':
                print(f"\n{odd_list(fib_list)}")
            case 'e':
                print(f"\n{even_list(fib_list)}")
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
            assert num_terms > 1
        except ValueError:
            if num_terms == 'q':
                exit("<<<Closing Fibonacci program>>>")
            else:
                print("\nThe quantity of desired terms must be 2 or greater.")
                pass
        except AssertionError:
            print("\nThe quantity of desired terms must be 2 or greater.")
        else:
            for _ in range(2, num_terms):
                fib_list.append(fib_list[_ - 2] + fib_list[_ - 1])
            return fib_list


def valid_menu_choice(choice) -> bool:
    match choice:
        case 'p' | 'u' | 'l' | 'o' | 'e' | 'n' | 'q':
            return True
        case _:
            return False


def main_menu_handler(fib_list: list) -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print(f"(p) Print your sequence of {len(fib_list)} numbers.")
        print("(u) Print all numbers less than or equal to a given upper bound.")
        print("(l) Print all numbers greater than or equal to a given lower bound.")
        print("(o) Print out all odd numbers in your list.")
        print("(e) Print out all even numbers in your list.")
        print("(n) Generate a new list.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice


def upper_bounded_list(fib_list: list) -> list:
    while True:
        try:
            upper_b = input("\nEnter your desired upper bound: ").strip()
            upper_b = int(upper_b)
        except ValueError:
            print(f"\nThe upper bound must be a whole number.")
            pass
        else:
            bounded_list = []
            for _ in fib_list:
                if _ <= upper_b:
                    bounded_list.append(_)
            return bounded_list


def lower_bounded_list(fib_list: list) -> list:
    while True:
        try:
            lower_b = input("\nEnter your desired lower bound: ").strip()
            lower_b = int(lower_b)
        except ValueError:
            print(f"\nThe lower bound must be a whole number.")
            pass
        else:
            bounded_list = []
            for _ in fib_list:
                if _ >= lower_b:
                    bounded_list.append(_)
            return bounded_list


def odd_list(fib_list: list) -> list:
    odd_terms = []
    for _ in fib_list:
        if _ % 2 == 1:
            odd_terms.append(_)
    return odd_terms


def even_list(fib_list: list) -> list:
    even_terms = []
    for _ in fib_list:
        if _ % 2 == 0:
            even_terms.append(_)
    return even_terms


if __name__ == "__main__":
    main()
    