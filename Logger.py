import logging
from datetime import datetime
import colorlog
from LiveTradingConfig import LOG_LEVEL, log_to_file
import os
import sys


def get_logger():
    # Создаем регистратор и устанавливаем его уровень на LOG_LEVEL
    log = logging.getLogger()
    log.setLevel(LOG_LEVEL)
    # Создаем форматтер с помощью ColoredFormatter от colorlog.
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)s: %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "bold_white",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    if log_to_file:
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
        )
        # Получить текущую дату и время
        current_datetime = datetime.now()
        # Форматируем дату и время с помощью подчеркиваний между элементами
        formatted_datetime = current_datetime.strftime("%d_%m_%Y_%H_%M_%S")
        # Создаём обработчик файлов и устанавливаем форматтер
        file_handler = logging.FileHandler(f"Live_Trading_{formatted_datetime}.log")
        file_handler.setFormatter(file_formatter)
        log.addHandler(file_handler)

    # Создаём обработчик консоли и устанавливаем форматтер
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    # Добавляем обработчик консоли в логгер
    log.addHandler(console_handler)
    return log


log = get_logger()

