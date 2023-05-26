import os
import logging

logger = logging.Logger(__name__)
def main():
    print(f"hello.py = {__name__}")
    x = int(input("What is x?"))
    print("Even" if isEven(x) else "Odd")
    print(f'The square of x is {square(x)}.')
    print("meow\n"*3,end="")

# def square(root):
#     return root**2
#
# def isEven(n):
#     return (n%2==0)


class MathFuncs:
    def __init__(self, input_param: int = 5):
        """
        This class contains helpful math functions

        :param input_param: Optional input parameter. Should be an int.
        """
        self.input_param_modified = input_param

    def square(self) -> int:
        try:
            return self.input_param_modified ** 2
        except TypeError as e:
            logger.warning(
                f"You can't square an int and a {type(self.input_param_modified)}!",
                exc_info=True
            )
            return self.input_param_modified * 2


    def is_even(self) -> bool:
        try:
            return self.input_param_modified % 2 == 0
        except TypeError:
            logger.warning(
                f"A {str(type(self.input_param_modified))} can't be evaluated as even or odd!"
            )
            if isinstance(self.input_param_modified, str):
                logger.info("But I can do this:")
                return len(self.input_param_modified) % 2 == 0


math_func_instance: MathFuncs = MathFuncs()
print("Working Instance\n________________\n")
print(math_func_instance.square())
print(math_func_instance.is_even())

# This is warning because the type hint says the input_param should be an int instead of a string
broken_obj = MathFuncs(input_param="dog")
print("Broken Instance\n________________\n")
print(broken_obj.square())
print(broken_obj.is_even())

# if __name__ == "__main__":
#     main()