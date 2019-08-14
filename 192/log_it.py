import logging
from typing import Callable

def DEBUG():
    return "DEBUG"

def INFO():
    return "INFO"

def WARNING():
    return "WARNING"

def ERROR():
    return "ERROR"

def CRITICAL():
    return "CRITICAL"


def log_it(level: Callable, msg: str) -> None:
    logger = logging.getLogger('pybites_logger')
    levelnum = logging.getLevelName(level())
    logger.log(levelnum, msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")