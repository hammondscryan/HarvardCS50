import datetime

def main():
    new_User = Person()
    #new_User.name = new_User.assign_name()
    #new_User.age = new_User.assign_age()

    current_year = datetime.date.today().year
    new_User_100th = new_User.calc_100th(current_year)
    if new_User_100th > current_year:
        print(f"{new_User.name}, your 100th birthday will be in {new_User_100th}!")
    elif new_User_100th == current_year:
        print(f"Have a happy 100th year, {new_User.name}!")
    else:
        print(f"{new_User.name}, your 100th birthday was in {new_User_100th}!")

class Person:
    name = "Stranger"
    age = 0
    def __int__(self, name: str ="Stranger",age: int =0):
        self.name = name
        self.age = age
    def assign_name(self) -> str:
        return input("Please enter your name:")
    def assign_age(self) -> int:
        acceptable_age = False
        test_age = input("Please enter your age in years:")
        while (not acceptable_age):
            if (test_age.isnumeric() and int(test_age) >= 0):
                acceptable_age = True
            else:
                print("Your age must a positive whole number of years.")
                test_age = input("Please re-enter your age:")
        return int(test_age)

    def calc_100th(self, current_year: int) -> int:
        return (current_year + (100-self.age))



if __name__=="__main__":
    main()