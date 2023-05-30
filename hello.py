import logging

logger = logging.Logger(__name__)


def main():
    print(f"hello.py = {__name__}")

    x = int(input("What is x?"))
    math_object = MathFuncs(x)

    print(f"{math_object.input_param} is even." if math_object.is_even() else f"{math_object.input_param} is odd.")
    print(f'The square of {math_object.input_param} is {math_object.square()}.')


class MathFuncs:
    def __init__(self, input_param: int = 1):
        """
        This class contains helpful math functions

        :param input_param: Optional input parameter. Should be an int.
        """
        self.input_param = input_param

    def square(self) -> int:
        try:
            return self.input_param ** 2
        except TypeError as e:
            logger.warning(
                f"You can't square a {type(self.input_param)}!",
                exc_info=True
            )

    def is_even(self) -> bool:
        try:
            return self.input_param % 2 == 0
        except TypeError:
            logger.warning(
                f"A {str(type(self.input_param))} can't be evaluated as even or odd!"
            )


if __name__ == "__main__":
    main()
