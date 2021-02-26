import os
from typing import NoReturn


def always_raises() -> NoReturn:
    """docstring for always_raises"""
    raise AssertionError("why did you call me?")


def calls_exec() -> NoReturn:
    """docstring for calls_exec"""
    os.execvp("echo", ("echo", "hi"))


def loops_forever() -> NoReturn:
    """docstring for loops_forever"""
    while True:
        request = get_request()
        handle_response(request)


def calls_something_with_noreturn() -> NoReturn:
    """docstring for calls_something_with_noreturn"""
    loops_forever()


def has_no_return_statements() -> None:
    """docstring for f"""
    print("hello world")


def explicitly_returns_none() -> None:
    """docstring for explicitly_returns_none"""
    return None
