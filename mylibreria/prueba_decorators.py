import functools


def dec(func):
    """docstring for dec"""

    @functools.wraps(func)
    def dec_inner(*args, **kwargs):
        """docstring for dec_inner"""
        print(f"got {args} {kwargs}")
        ret = func(*args, **kwargs)
        print("after")
        return ret

    return dec_inner


def dec2(greeting, farewall):
    """docstring for dec2"""

    def dec2_decorator(func):
        """docstring for dec2_decorator"""

        @functools.wraps(func)
        def dec2_inner(*args, **kwargs):
            """docstring for dec2_inner"""
            print(greeting)
            ret = func(*args, **kwargs)
            print(farewall)
            return ret

        return dec2_inner

    return dec2_decorator


@dec2("hello", "goodbye")
def f(x: int) -> None:
    """docstring for f"""
    print(f"hello {x}")


class C:
    """description"""

    def __init__(self, x):
        self.x = x

    @property
    def y(self):
        """docstring for y"""
        print("in property y")
        return self.x + 5

    @classmethod
    def func(cls):
        """docstring for func"""
        print(f"in class {cls}")

    @staticmethod
    def func():
        """docstring for func"""
        print("normal function")


def main():
    """docstring for main"""
    f(1)


if __name__ == "__main__":
    exit(main())
