
def main():

    all_sets = dict()
    print_intro()
    while True:
        menu_choice = main_menu_handler()
        print('\n')
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
    def __init__(self, name: str = str(), element_list: list = list()):
        self.name = name
        self.element_list = element_list
        self.multiplicity_table = dict()
        for element in element_list:
            if str(element) not in self.multiplicity_table:
                self.multiplicity_table[str(element)] = 1
            else:
                self.multiplicity_table[str(element)] += 1

    def update_set(self, element_list: list = list(),
                   multiplicity_table: dict = dict(),
                   name: str = str(),
                   option: str = 'e'):
        match option:
            case 'e':
                self.element_list = element_list
                self.multiplicity_table.clear()
                for element in self.element_list:
                    if str(element) not in self.multiplicity_table:
                        self.multiplicity_table[str(element)] = 1
                    else:
                        self.multiplicity_table[str(element)] += 1
            case 'm':
                self.multiplicity_table = multiplicity_table
                self.element_list.clear()
                for element in self.multiplicity_table:
                    for _ in range(multiplicity_table[element]):
                        self.element_list.append(float(element))
            case 'n':
                self.name = name

    def add_element(self, new_element: float):
        self.element_list.append(new_element)
        self.update_set(self.element_list)

    def del_element(self, element: float):
        if element in self.element_list:
            self.element_list.remove(element)
            self.update_set(self.element_list)

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
    menu_choice = str()
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
    while True:
        try:
            print(f"There are {len(all_sets)} sets available.")
            choice = input("Type the name of the set to display.\n"
                           "Type @ to print all sets or < to return to the menu.").strip()
            assert choice in all_sets or choice == '@' or choice == '<'
        except AssertionError:
            print("Please type a valid set name.\n".upper())
            pass
        else:
            if choice == '<':
                print("Returning to the main menu.".upper())
            elif choice == '@':
                print('\n')
                if len(all_sets) == 0:
                    print(f"There are no defined sets!".upper())
                else:
                    for entry in all_sets:
                        print(f"{entry} -> {all_sets[entry].element_list}")
            else:
                print('\n')
                print(f"{choice} -> {all_sets[choice].element_list}")
            break


def multiplicity(all_sets: dict):
    results = dict()
    while True:
        try:
            element = input("Which element are you finding the multiplicity of?\n"
                            "Type < to return to the menu.").strip()
            if element == '<':
                print("Returning to the main menu.".upper())
                break
            else:
                element = float(element)
        except ValueError:
            print("Please enter a real number.\n".upper())
            pass
        else:
            choice = input("Name the sets you would like to check (separated by commas).\n"
                           "Type @ to check all sets or < to return to the menu.").strip()
            if choice == '<':
                print("Returning to the main menu.".upper())
            elif choice == '@':
                for a_set in all_sets:
                    if str(element) not in all_sets[a_set].multiplicity_table:
                        results[a_set] = 0
                    else:
                        results[a_set] = all_sets[a_set].multiplicity_table[str(element)]
                print(f"The multiplicity of {element} in all sets is:\n",
                      f"{results}")
                return
            else:
                sets_to_check = [x.strip() for x in choice.split(',')]
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        results[a_set] = "SET NOT FOUND"
                    elif str(element) not in all_sets[a_set].multiplicity_table:
                        results[a_set] = 0
                    else:
                        results[a_set] = all_sets[a_set].multiplicity_table[str(element)]
                print(f"The multiplicity of of {element} in {sets_to_check} is:\n"
                      f"{results}")
                return
            break


def add_set(all_sets: dict):
    set_name = str()
    while True:
        try:
            set_name = input("Enter the name of your new set (cannot contain @ or <).\n"
                             "Type < to return to the menu.").strip()
            if set_name == '<':
                print("Returning to the main menu.".upper())
                break
            assert set_name.find('<') < 0 and set_name.find('@') < 0 and set_name not in all_sets
        except AssertionError:
            if set_name in all_sets:
                print("A set with that name already exists. Please choose another name.".upper())
            else:
                print("Your set name may cannot contain @ or <.".upper())
            pass
        else:
            choice = input("List the desired elements (separated by commas, duplicates allowed).\n"
                           "Type < to return to the menu.").strip()
            if choice == '<':
                print("Returning to the main menu.".upper())
            else:
                element_list = [x.strip() for x in choice.split(',')]
                try:
                    for i, entry in enumerate(element_list):
                        element_list[i] = float(entry)
                except ValueError:
                    print("All set elements must be real numbers.".upper())
                    break
                else:
                    all_sets[set_name] = Set(set_name, element_list)
                    print(f"Success! {set_name} has been added.")
            break


def delete_set(all_sets: dict):
    while True:
        print(f"There are {len(all_sets)} sets available.")
        choice = input("Type the names of the sets to delete.\n"
                       "Type @ to delete all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.".upper())
            break
        elif choice == '@':
            all_sets.clear()
            print("All sets deleted.".upper())
            return
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                for a_set in sets_to_check:
                    assert a_set in all_sets
            except AssertionError:
                error_list = list()
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}. Please enter your list again.".upper())
            else:
                for a_set in sets_to_check:
                    del all_sets[a_set]
                print(f"The following sets were deleted: {sets_to_check}.")
                break


def intersection(all_sets: dict):
    ix_set = dict()
    results = dict()
    while True:
        choice = input("Which sets would you like to intersect (separated by commas)?\n"
                       "Type @ to intersect all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.".upper())
            break
        elif choice == '@':
            for i, a_set in enumerate(all_sets):
                if i == 0:
                    ix_set = all_sets[a_set].multiplicity_table.copy()
                else:
                    for element in ix_set:
                        if element in all_sets[a_set].multiplicity_table:
                            ix_set[element] = min(ix_set[element], all_sets[a_set].multiplicity_table[element])
                        else:
                            ix_set[element] = 0
            for element in ix_set:
                if ix_set[element] != 0:
                    results[element] = ix_set[element]
            if len(results) == 0:
                print(f"These intersection of all sets is empty.")
            else:
                print(f"The intersection of all sets is {parse_multiplicity_table(results)}.")
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                for i, a_set in enumerate(sets_to_check):
                    if i == 0:
                        ix_set = all_sets[a_set].multiplicity_table
                    else:
                        for element in ix_set:
                            if element in all_sets[a_set].multiplicity_table:
                                ix_set[element] = min(ix_set[element], all_sets[a_set].multiplicity_table[element])
                            else:
                                ix_set[element] = 0
                for element in ix_set:
                    if ix_set[element] != 0:
                        results[element] = ix_set[element]
                if len(results) == 0:
                    print(f"These intersection of the following sets is empty.\n"
                          f"{sets_to_check}")
                else:
                    print(f"The intersection of {sets_to_check} is:\n"
                          f"{parse_multiplicity_table(results)}")
            except KeyError:
                error_list = list()
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.".upper())
        break


def union(all_sets: dict):
    union_set = list()
    while True:
        choice = input("Which sets would you like to union (separated by commas)?\n"
                       "Type @ to union all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.".upper())
            break
        elif choice == '@':
            for a_set in all_sets:
                union_set += all_sets[a_set].element_list
            if len(union_set) == 0:
                print(f"The union of all sets is empty.")
            else:
                print(f"The union of all sets is {union_set}.")
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                for a_set in sets_to_check:
                    union_set += all_sets[a_set].element_list
                if len(union_set) == 0:
                    print("The union of the following sets is empty:"
                          f"{sets_to_check}")
                print(f"The union of {sets_to_check} is:\n"
                      f"{union_set}")
                return
            except KeyError:
                error_list = list()
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.".upper())
        break


def max_calc(all_sets: dict):
    while True:
        choice = input("Which set or sets would you like to analyze (separated by commas)?\n"
                       "Type @ to check all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.".upper())
            break
        elif choice == '@':
            max_elements = list()
            for a_set in all_sets:
                max_elements.append(all_sets[a_set].maximum())
            print(f"{max(max_elements)} is the maximum value across all sets.\n")
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                max_elements = list()
                for a_set in sets_to_check:
                    max_elements.append(all_sets[a_set].maximum())
                print(f"{max(max_elements)} is the maximum value of the following sets:\n"
                      f"{sets_to_check}")
                return
            except KeyError:
                error_list = list()
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.".upper())
        break


def min_calc(all_sets: dict):
    while True:
        choice = input("Which set or sets would you like to analyze (separated by commas)?\n"
                       "Type @ to check all sets or < to return to the menu.").strip()
        if choice == '<':
            print("Returning to the main menu.".upper())
            break
        elif choice == '@':
            min_elements = list()
            for a_set in all_sets:
                min_elements.append(all_sets[a_set].minimum())
            print(f"{min(min_elements)} is the minimum value across all sets.\n")
        else:
            sets_to_check = [x.strip() for x in choice.split(',')]
            try:
                min_elements = list()
                for a_set in sets_to_check:
                    min_elements.append(all_sets[a_set].minimum())
                print(f"{min(min_elements)} is the minimum value of the following sets:\n"
                      f"{sets_to_check}")
                return
            except KeyError:
                error_list = list()
                for a_set in sets_to_check:
                    if a_set not in all_sets:
                        error_list.append(a_set)
                print(f"The following sets do not exist: {error_list}.".upper())
        break


def parse_multiplicity_table(m_table: dict) -> list:
    e_list = list()
    for element in m_table:
        for _ in range(m_table[element]):
            e_list.append(float(element))
    return e_list


def create_multiplicity_table(e_list: list) -> dict:
    m_table = dict()
    for element in e_list:
        if str(element) not in m_table:
            m_table[str(element)] = 1
        else:
            m_table[str(element)] += 1
    return m_table


if __name__ == "__main__":
    main()
