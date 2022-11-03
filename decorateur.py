import functools
import time
import logging


def decorateur(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            filename="log",
            format="%(asctime)s - %(message)s",
            level=logging.INFO
        )
        logging.info("%s started", function.__name__)
        result = function(*args, *kwargs)
        logging.info("%s ended", function.__name__)
        return result
    return wrapper

# def decorateur(function):
#     @functools.wraps(function)
#     def timer(*args, **kwargs):
#         with open("log", "a", encoding="utf-8") as file:
#             ts = datetime.datetime.now()
#             file.write(function.__name__ +
#                        ts.strftime(" start at %H:%M:%S.%f\n"))
#         result = function(*args, *kwargs)
#         with open("log", "a", encoding="utf-8") as file:
#             ts = datetime.datetime.now()
#             file.write(function.__name__ +
#                        ts.strftime(" end at %H:%M:%S.%f\n"))
#         return result
#     return timer


@decorateur
def c(second: int):
    """function that pause the programme

    Args:
        second (int): nomber of second
    """
    time.sleep(second)


@decorateur
def b(second: int):
    c(second)


@decorateur
def a(second: int):
    b(second)


a(2)
