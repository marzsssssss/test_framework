import logging
import os

class Logger:
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, "reports")
    LOG_FILE = os.path.join(LOG_DIR, "test_framework.log")

    def __init__(self, name: str):
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)

        # Проверяем, чтобы обработчики не добавлялись повторно
        if not self._logger.handlers:
            formatter = logging.Formatter(self.LOG_FORMAT)

            file_handler = logging.FileHandler(self.LOG_FILE, mode="a", encoding="utf-8")
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self._logger.addHandler(stream_handler)

    def get(self) -> logging.Logger:
        return self._logger