import logging
from abc import ABC

from .color_ascii import Style


class BaseColorFormatter(logging.Formatter, ABC):
    COLORS = {}

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, Style.RESET)
        record.levelname = f"{color}{record.levelname}{Style.RESET}"
        return super().format(record)
