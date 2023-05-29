def main():
    print_intro()
    fib_list = create_fib_list()
    if fib_list is None:
        print("\n<<<Closing Fibonacci program>>>")
    else:
        menu_choice = ''
        while menu_choice != 'q':
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
                    if fib_list is None:
                        menu_choice = 'q'
                        print("<<<Closing Fibonacci program>>>")
                case 'q':
                    print("<<<Closing Fibonacci program>>>")


def print_intro():
    print("\n\n\nThis program generates the first n entries of the Fibonacci sequence!")
    print("Remember that the first two entries in the sequence will always be 1.")
    print("So, n should be greater than or equal to 2.")
    print("Enter q to quit.")

def create_fib_list():
    fib_list = [1,1]
    num_entries = input("\nHow many entries in the sequence would you like to generate (or q to quit)?").strip()
    if num_entries != 'q':
        while not str.isnumeric(num_entries) or int(num_entries) < 2:
            print("\nThe quantity of desired entries must be a whole number greater than 2.")
            num_entries = input("Please re-enter your desired sequence length (or q to quit): ").strip()
        if num_entries != 'q':
            num_entries = int(num_entries)
            for _ in range(2,num_entries):
                fib_list.append(fib_list[_-2]+fib_list[_-1])
            return fib_list
    else:
        break
    return None


def valid_menu_choice(choice) -> bool:
    if choice == 'p' or choice == '<' or choice =='o' or choice == 'e' or choice == 'n' or choice =='q':
        return True
    else:
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
    upper_b = input("\nEnter your desired upper bound: ").strip()
    while not str.isnumeric(upper_b) or int(upper_b)>fib_list[len(fib_list) - 1 or int(upper_b)<1]:
        print(f"\nThe maximum value must be a whole number between 1 and {fib_list[len(fib_list)-1]}, inclusive.")
        upper_b = input("Please re-enter your desired upper bound: ").strip()
    upper_b = int(upper_b)
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