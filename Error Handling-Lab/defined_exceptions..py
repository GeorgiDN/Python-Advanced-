class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""


num = int(input())


if num < 10:
    raise ValueTooSmallError
elif num >= 10:
    print(num)
