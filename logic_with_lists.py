def main():
    print(f"This is {__name__}.")
    intro()
    new_set = define()
    '''
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

'''
def create_set() -> list:
    new_set = []
'''
    new_set = input("\nEnter a positive integer to factorize (or q to quit): ").strip()
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
'''


def intro():
    print("\n\n\nThis program performs basic set logic.")
    print("It is assumed that every set contains real numbers (duplicates will be deleted).")


def valid_menu_choice(choice) -> bool:
    if choice == 'p'|'n'|'d'|'i'|'u'|'M'|'m'|'q':
        return True
    else:
        return False


def main_menu_handler(new_set: list) -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print(f"(p) Print a set.")
        print("(n) Add a new set.")
        print("(d) Delete a set.")
        print("(i) Give the intersection of defined sets.")
        print("(u) Give the union of defined sets.")
        print("(M) Calculate the maximum of a given set.")
        print("(m) Calculate the minimum of a given set.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice

class Set:
    def __init__(self, contents: list =[]):
        self.contents = contents

    def define(self):
        #prompt to ingest a series of real numbers
        #check to ensure that these numbers are actually real numbers and not alpha
        #handle errors
        #assign set to class attrib AND return Bool to indicate success/failure



if __name__ == "__main__":
    main()
