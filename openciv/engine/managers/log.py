import logging
import os
import sys
from datetime import datetime
from typing import Callable, Union
from openciv.engine.mixins.singleton import Singleton


class LogManager(Singleton):
    def __setup__(self, debug_mode: bool = True, testing_mode: bool = False):
        self.debug_mode = debug_mode
        self.testing_mode = testing_mode
        self.loggers = {}
        self.setup_loggers()
        self.redirect_output_to_debug()

    def setup_loggers(self):
        log_types = {
            "gameplay": logging.INFO,
            "engine": logging.DEBUG,
            "graphics": logging.INFO,
            "misc": logging.DEBUG,
            "debug": logging.DEBUG,
            "ursina": logging.DEBUG,
        }

        for log_type, level in log_types.items():
            logger = logging.getLogger(log_type)
            logger.setLevel(level)

            # Remove all handlers associated with the logger
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

            # Create log directory structure
            log_dir = f"logs/{log_type}"
            os.makedirs(log_dir, exist_ok=True)
            if self.testing_mode:
                log_file = os.path.join(log_dir, f'test_log_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log')
            else:
                log_file = os.path.join(log_dir, f'log_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log')

            # Create file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)

            # Create formatter and add it to the handlers
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Add stream handler if in debug mode and not testing mode
            if self.debug_mode and not self.testing_mode:
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(logging.DEBUG)
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)

            self.loggers[log_type] = logger

    def redirect_output_to_debug(self):
        """
        Redirects the stdout and stderr to the engine logger.
        """

        class RedirectOutput:
            """
            A class to redirect stdout to a logger instance with a specified log level.

            Attributes:
                logger (logging.Logger): The logger instance where the messages are redirected.
                method (Union[Callable, str]): The logging method to use for output.
                buffer (str): Buffer to store messages before logging.
            """

            def __init__(
                self, logger: logging.Logger, method: Union[Callable, str] = "debug", testing_mode: bool = False
            ):
                self.logger = logger
                self.buffer = ""
                self.testing_mode = testing_mode

                # Set the logging method based on the provided method argument
                if isinstance(method, str):
                    self.log_method = getattr(logger, method)
                else:
                    self.log_method = method

            def write(self, message: str):
                """
                Write the message to the buffer. Logs each line when a newline is encountered.

                Args:
                    message (str): The message to write to the buffer.
                """
                if not self.testing_mode:
                    self.buffer += message
                    while "\n" in self.buffer:
                        line, self.buffer = self.buffer.split("\n", 1)
                        self.log_method(line)

            def flush(self):
                """
                Flush the buffer, logging any remaining messages.
                """
                if not self.testing_mode and self.buffer:
                    self.log_method(self.buffer)
                    self.buffer = ""

        sys.stdout = RedirectOutput(self.ursina, "debug", self.testing_mode)
        sys.stderr = RedirectOutput(self.ursina, "error", self.testing_mode)

    def log(self, log_type: str, message: str):
        if log_type in self.loggers:
            self.loggers[log_type].info(message)
        else:
            raise ValueError(f"Unknown log type: {log_type}")

    def error(self, log_type: str, message: str):
        if log_type in self.loggers:
            self.loggers[log_type].error(message)
        else:
            raise ValueError(f"Unknown log type: {log_type}")

    def logger(self, logger) -> logging.Logger:
        return self.loggers[logger]

    def set_testing_mode(self, testing_mode: bool):
        """
        Sets the testing mode and reconfigures the loggers and output redirection.

        Args:
            testing_mode (bool): Flag to enable or disable testing mode.
        """
        self.testing_mode = testing_mode
        self.setup_loggers()
        self.redirect_output_to_debug()

    @property
    def gameplay(self) -> logging.Logger:
        return self.loggers["gameplay"]

    @property
    def engine(self) -> logging.Logger:
        return self.loggers["engine"]

    @property
    def graphics(self) -> logging.Logger:
        return self.loggers["graphics"]

    @property
    def misc(self) -> logging.Logger:
        return self.loggers["misc"]

    @property
    def debug(self) -> logging.Logger:
        return self.loggers["debug"]

    @property
    def ursina(self) -> logging.Logger:
        return self.loggers["ursina"]
