import datetime


def main():
    new_user = User()
    new_user.name = new_user.assign_name()
    new_user.age = new_user.assign_age()

    current_year = datetime.date.today().year
    new_user_100th = new_user.calc_100th(current_year)
    if new_user_100th > current_year:
        print(f"{new_user.name}, your 100th birthday will be in {new_user_100th}!")
    elif new_user_100th == current_year:
        print(f"Have a happy 100th year, {new_user.name}!")
    else:
        print(f"{new_user.name}, your 100th birthday was in {new_user_100th}!")


class User:
    def __init__(self, name: str ="Stranger", age: int =0):
        self.name = name
        self.age = age

    def assign_name(self) -> str:
        return input("Please enter your name:")

    def assign_age(self) -> int:
        acceptable_age = False
        test_age = input("Please enter your age in years:")
        while not acceptable_age:
            if test_age.isnumeric() and int(test_age) >= 0:
                acceptable_age = True
            else:
                print("Your age must a positive whole number of years.")
                test_age = input("Please re-enter your age:")
        return int(test_age)

    def calc_100th(self, current_year: int) -> int:
        return current_year + (100-self.age)


if __name__ == "__main__":
    main()
