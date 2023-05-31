import datetime


def main():
    new_user = User()
    new_user.assign_name()
    new_user.assign_age()

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

    def assign_name(self):
        self.name = str.strip(input("Please enter your name:"))

    def assign_age(self):
        test_age = -1
        #Fix the code so that an appropriate msg is printed if the user enters a negative number
        while True:
            try:
                test_age = int(input("Please enter your age in years.").strip())
            except ValueError:
                print("\nYour age must a positive whole number of years.")
                pass
            else:
                if test_age < 0:
                    print("\nYour age must a positive whole number of years.")
                else:
                    break

        self.age = test_age

    def calc_100th(self, current_year: int) -> int:
        return current_year + (100-self.age)


if __name__ == "__main__":
    main()
