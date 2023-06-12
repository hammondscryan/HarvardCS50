import itertools

def main():

    #all_sets is a dictionary whose values are instances of the class Set.
    #the keys are the names of each set (Set.name)
    all_sets = {}
    print_intro()
    while True:
        menu_choice = main_menu_handler()
        match menu_choice:
            case 'p':
                print_set(all_sets)
            case 'x':
                multiplicity(all_sets)
            case 'n':
                add_set(all_sets)
            case 'd':
                delete_set(all_sets)
            case 'i':
                intersection(all_sets)
            case 'u':
                union(all_sets)
            case 'M':
                max_calc(all_sets)
            case 'm':
                min_calc(all_sets)
            case 'q':
                exit("<<<Closing Set Logic Program>>>")


class Set:
    #An alphanumeric name for the set: @ and < are not allowed in the name
    name = str()

    #The set of all elements
    element_list = list()

    #The key is the set entry, while the values indicate the number of times that item occurs in the set
    multiplicity_table = dict()

    def __init__(self, name: str, element_list: list):
        self.name = name
        self.element_list = element_list
        for element in self.element_list:
            if str(element) not in self.multiplicity_table:
                self.multiplicity_table[str(element)] = 1
            else:
                self.multiplicity_table[str(element)] += 1


    def update_set(self, element_list: list):
        self.element_list = element_list
        self.multiplicity_table.clear()
        for element in self.element_list:
            if str(element) not in self.multiplicity_table:
                self.multiplicity_table[str(element)] = 1
            else:
                self.multiplicity_table[str(element)] += 1

    def add_element(self, new_element: float):
        self.update_set(self.element_list.append(new_element))

    def del_element(self, element: float):
        if element in self.element_list:
            self.update_set(self.element_list.remove(element))

    def magnitude(self, option='e') -> int:
        match option:
            case 'e':
                return len(self.element_list)
            case 'm':
                return len(self.multiplicity_table)

    def maximum(self) -> float:
        if self.magnitude() > 0:
            return max(self.element_list)
        else:
            return None

    def minimum(self) -> float:
        if self.magnitude() > 0:
            return min(self.element_list)
        else:
            return None



def print_intro():
    print("\n\n\nThis program performs basic set logic on unordered sets (duplication allowed).")
    print("Sets here must contain real numbers (or be empty).")
    print("Enter q to quit.")


def main_menu_handler() -> str:
    menu_choice = ''
    while not valid_menu_choice(menu_choice):
        print("\n<<<MAKE A SELECTION>>>")
        print("(p) Print a set.")
        print("(x) Display the multiplicity of an element in a set.")
        print("(n) Add a new set.")
        print("(d) Delete a set.")
        print("(i) Give the intersection of sets.")
        print("(u) Give the union of sets.")
        print("(M) Calculate the maximum of a set or list of sets.")
        print("(m) Calculate the minimum of a set or list of sets.")
        print("(q) End program.")
        menu_choice = input("SELECTION: ").strip()
    return menu_choice


def valid_menu_choice(choice) -> bool:
    match choice:
        case 'p' | 'x' | 'n' | 'd' | 'i' | 'u' | 'M' | 'm' | 'q':
            return True
        case _:
            return False

def print_set(all_sets: dict):
    print(f"There are {len(all_sets)} sets available.")
    while True:
        try:
            choice = input("Type the name of the set to display.\n"
                           "Type @ to print all sets or < to return to the menu.").strip()
            assert choice in all_sets or choice == '@' or choice == '<'
        except AssertionError:
            print("Please type the name of the set to display.\n"
                  "You may type @ to print all sets or < to return to the menu.")
            pass
        else:
            if choice == '<':
                print("Returning to the main menu.")
            elif choice == '@':
                for entry in all_sets:
                    print(all_sets[entry].element_list)
            else:
                print(all_sets[choice].element_list)
            break


def multiplicity(all_sets: dict):
    while True:
        try:
            element = input("Which element are you finding the multiplicity of?\n"
                           "Type < to return to the menu.").strip()
            float(element)
        except ValueError:
            if(element == '<'):
                print("Returning to the main menu.")
                break
            else:
                print("Please enter a real number.\n"
                      "You may type < to return to the menu.")
            pass
        else:
            results = {}
            choice = input("Name the sets you would like to check (separated by commas).\n"
                           "Type @ to check all sets or < to return to the menu.").strip()
            if choice == '<':
                print("Returning to the main menu.")
            elif choice == '@':
                for a_set in all_sets:
                    if element not in all_sets[a_set].multiplicity_table:
                        results[a_set] = 0
                    else:
                        results[a_set] = all_sets[a_set].multiplicity_table[str(element)]
                print(results)
            else:
                sets_to_check = [x.strip() for x in choice.split(',')]
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        results[a_set] = "SET NOT FOUND"
                    elif element not in all_sets[a_set].multiplicity_table:
                        results[a_set] = 0
                    else:
                        results[a_set] = all_sets[a_set].multiplicity_talbe[str(element)]
                print(results)
            break





def add_set(all_sets: dict) -> Set:
    while True:
        try:
            set_name = input("Enter the name of your new set (cannot contain @ or <).\n"
                             "Type < to return to the menu.").strip()
            assert set_name.find('<') < 0 and set_name.find('@') < 0 and set_name not in all_sets
        except AssertionError:
            if set_name == '<':
                print("Returning to the main menu.")
                break
            elif set_name in all_sets:
                print("A set with that name already exists. Please choose another name.")
            else:
                print("Your set name may cannot contain @ or <.")
            pass
        else:
            results = Set(set_name)
            choice = input("List the desired elements (separated by commas, duplicates allowed).\n"
                           "Type < to return to the menu.").strip()
            if choice == '<':
                print("Returning to the main menu.")
            else:
                element_list = [x.strip() for x in choice.split(',')]
                try:
                    for _, entry in enumerate(element_list):
                        element_list[_] = float(entry)
                except TypeError:
                    print("All set elements must be real numbers.")
                    pass
                else:
                    results.update_set(element_list)
                    all_sets[results.name] = results
                    break


def delete_set(all_sets: dict) -> list:
    print("delete_set()")
    return True


def intersection(all_sets: dict):
    print("intersection()")
    return True


def union(all_sets: dict):
    print("union()")
    return True


def max_calc(all_sets: dict):
    while True:
        choice = input("Which set or sets would you like to analyze (separated by commas)?\n"
                       "Type @ to check all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.")
            break
        elif choice == '@':
            max_element = float()
            for a_set in all_sets:
                if max_element < all_sets[a_set].maximum():
                    max_element = all_sets[a_set].maximum()
            return max_element
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                max_element = float()
                for a_set in sets_to_check:
                    if max_element < all_sets[a_set].maximum():
                        max_element = all_sets[a_set].maximum()
                return max_element
            except KeyError:
                error_list = []
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.")
                break



def min_calc(all_sets: dict):
    while True:
        choice = input("Which set or sets would you like to analyze (separated by commas)?\n"
                       "Type @ to check all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.")
            break
        elif choice == '@':
            min_element = float()
            for a_set in all_sets:
                if min_element > all_sets[a_set].minimum():
                    min_element = all_sets[a_set].minimum()
            return min_element
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                min_element = float()
                for a_set in sets_to_check:
                    if min_element > all_sets[a_set].minimum():
                        min_element = all_sets[a_set].minimum()
                return min_element
            except KeyError:
                error_list = []
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.")
                break


if __name__ == "__main__":
    main()
