from .base_color_formatter import BaseColorFormatter
from .color_ascii import HighIntensityBackground, Standard, Style


class DefaultColorFormatter(BaseColorFormatter):
    COLORS = {
        "DEBUG": Standard.CYAN,
        "INFO": Standard.GREEN,
        "WARNING": Standard.YELLOW,
        "ERROR": Standard.RED,
        "CRITICAL": HighIntensityBackground.RED,
        "RESET": Style.RESET,
    }
