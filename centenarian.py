import datetime


def main():
    new_user = User()
    new_user.assign_name()
    new_user.assign_age()

    current_year = datetime.date.today().year
    new_user_100th = new_user.calc_100th(current_year)
    if new_user_100th > current_year:
        print(f"Howdy, {new_user.name}! Your 100th birthday will be in {new_user_100th}.")
    elif new_user_100th == current_year:
        print(f"Have a happy 100th year, {new_user.name}!")
    else:
        print(f"Howdy, {new_user.name}! Your 100th birthday was in {new_user_100th}.")


class User:
    def __init__(self, name: str = "Stranger", age: int = 0):
        self.name = name
        self.age = age

    def assign_name(self):
        self.name = str.strip(input("Please enter your name:"))
        if not self.name:
            self.name = 'Stranger'

    def assign_age(self):
        while True:
            try:
                test_age = input("Please enter your age in years.").strip()
                if test_age:
                    test_age = int(test_age)
                    assert test_age >= 0
            except ValueError:
                print("\nYour age must be a non-negative whole number of years.")
                pass
            except AssertionError:
                print("\nYour age must be a non-negative whole number of years.")
                pass
            else:
                if not test_age:
                    self.age = 0
                else:
                    self.age = test_age
                return

    def calc_100th(self, current_year: int) -> int:
        return current_year + (100-self.age)


if __name__ == "__main__":
    main()
