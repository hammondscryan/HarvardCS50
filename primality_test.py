from factorization import create_factors_list


def main():
    intro()
    while True:
        menu_choice = main_menu_handler()
        match menu_choice:
            case 'n':
                num, prime = primality()
                if prime:
                    print(f"{num} is a prime number.")
                else:
                    print(f"{num} is NOT a prime number.")
            case 'q':
                exit("<<<Closing factorization program>>>".upper())


def intro():
    print("\n\n\nThis program determines whether or not a positive integer is prime.")


def valid_menu_choice(choice) -> bool:
    match choice:
        case 'n' | 'q':
            return True
        case _:
            return False


def main_menu_handler() -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print("(n) Determine the primality of a new positive integer.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice


def primality():
    while True:
        try:
            num = input("\nEnter a positive integer (or q to quit): ").strip()
            num = int(num)
            assert num > 0
        except ValueError:
            if num == 'q':
                exit("<<<Closing factorization program>>>".upper())
            else:
                print("\nYou must enter a positive integer (i.e., whole number greater than 0).".upper())
                pass
        except AssertionError:
            print("\nYou must enter a positive integer (i.e., whole number greater than 0).".upper())
            pass
        else:
            if num == 1 or len(create_factors_list(num)) == 2:
                return num, True
            else:
                return num, False


if __name__ == "__main__":
    main()
