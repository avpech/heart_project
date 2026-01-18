import logging
import logging.config
import os


def setup_logging() -> None:
    os.makedirs("logs", exist_ok=True)
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "Console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "File": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "logs/app.log",
                "encoding": "utf-8",
            },
        },
        "loggers": {
            "": {
                "handlers": ["Console", "File"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(logging_config)
