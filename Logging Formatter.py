# Standard libs
from enum import Enum

# Local Imports
import config # Adds a local import to set a show debug flag in the config.py

# Determine warning levels
class Warninglevels(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRIT_ERROR = 4

# Check the SHOWDEBUG flag in config.py
ShowDebug = config.SHOWDEBUG

grey = "\x1b[38;20m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"


# Function to format a string
def format(string : str, level : Warninglevels = Warninglevels.DEBUG) -> str: # Set Debug as default warning level
    formatted_string = ""
    if level == Warninglevels.DEBUG:
        formatted_string = grey + "[DEBUG]: " + string + reset
    elif level == Warninglevels.INFO:
        formatted_string = grey + "[INFO]: " + string + reset
    elif level == Warninglevels.WARNING:
        formatted_string = yellow + "[WARNING]: " + string + reset
    elif level == Warninglevels.ERROR:
        formatted_string = red + "[ERROR]: " + string + reset
    elif level == Warninglevels.CRIT_ERROR:
        formatted_string = bold_red + "[CRITICAL ERROR]: " + string + reset
    else:
        raise ValueError("Invalid warning level")
    return formatted_string

# Function to format and log in the console
def notify(string : str, level : Warninglevels = Warninglevels.DEBUG) -> None: # Set Debug as default warning level
    if level == Warninglevels.DEBUG:
        if ShowDebug:
            print(format(string=string, level=level))
    else:
        print(format(string=string, level=level))
