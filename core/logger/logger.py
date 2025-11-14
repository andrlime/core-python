import logging
import sys

from .base_color_formatter import BaseColorFormatter
from .default_color_formatter import DefaultColorFormatter
from .log_level import LogLevel


def get_logger(
    name: str,
    level: LogLevel = LogLevel.INFO,
    formatter: type[BaseColorFormatter] = DefaultColorFormatter,
) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        fmt = formatter("%(asctime)s [%(levelname)s / %(name)s] %(message)s")
        handler.setFormatter(fmt)
        handler.setLevel(level.value)
        logger.addHandler(handler)

    logger.setLevel(level.value)
    return logger
