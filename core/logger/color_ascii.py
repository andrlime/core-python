"""
Several enums that contain all ASCII colors for printing in a shell
"""

from enum import StrEnum
from typing import Union


class Standard(StrEnum):
    BLACK = "\x1b[030m"
    RED = "\x1b[031m"
    GREEN = "\x1b[032m"
    YELLOW = "\x1b[033m"
    BLUE = "\x1b[034m"
    PURPLE = "\x1b[035m"
    CYAN = "\x1b[036m"
    WHITE = "\x1b[037m"


class Bold(StrEnum):
    BLACK = "\x1b[130m"
    RED = "\x1b[131m"
    GREEN = "\x1b[132m"
    YELLOW = "\x1b[133m"
    BLUE = "\x1b[134m"
    PURPLE = "\x1b[135m"
    CYAN = "\x1b[136m"
    WHITE = "\x1b[137m"


class Underline(StrEnum):
    BLACK = "\x1b[430m"
    RED = "\x1b[431m"
    GREEN = "\x1b[432m"
    YELLOW = "\x1b[433m"
    BLUE = "\x1b[434m"
    PURPLE = "\x1b[435m"
    CYAN = "\x1b[436m"
    WHITE = "\x1b[437m"


class StandardBackground(StrEnum):
    BLACK = "\x1b[40m"
    RED = "\x1b[41m"
    GREEN = "\x1b[42m"
    YELLOW = "\x1b[43m"
    BLUE = "\x1b[44m"
    PURPLE = "\x1b[45m"
    CYAN = "\x1b[46m"
    WHITE = "\x1b[47m"


class HighIntensity(StrEnum):
    BLACK = "\x1b[090m"
    RED = "\x1b[091m"
    GREEN = "\x1b[092m"
    YELLOW = "\x1b[093m"
    BLUE = "\x1b[094m"
    PURPLE = "\x1b[095m"
    CYAN = "\x1b[096m"
    WHITE = "\x1b[097m"


class BoldHighIntensity(StrEnum):
    BLACK = "\x1b[190m"
    RED = "\x1b[191m"
    GREEN = "\x1b[192m"
    YELLOW = "\x1b[193m"
    BLUE = "\x1b[194m"
    PURPLE = "\x1b[195m"
    CYAN = "\x1b[196m"
    WHITE = "\x1b[197m"


class HighIntensityBackground(StrEnum):
    BLACK = "\x1b[0100m"
    RED = "\x1b[0101m"
    GREEN = "\x1b[0102m"
    YELLOW = "\x1b[0103m"
    BLUE = "\x1b[0104m"
    PURPLE = "\x1b[0105m"
    CYAN = "\x1b[0106m"
    WHITE = "\x1b[0107m"


class Style(StrEnum):
    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"
    ITALIC = "\x1b[3m"
    UNDERLINE = "\x1b[4m"
    STRIKETHROUGH = "\x1b[9m"


ColorType = Union[
    Standard, Bold, Underline, StandardBackground, HighIntensity, BoldHighIntensity, HighIntensityBackground, Style
]
