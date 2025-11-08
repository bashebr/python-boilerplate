from logging.config import dictConfig


def setup_logging(level: str = "INFO", json: bool = False) -> None:
    formatter = (
        '{"level": "%(levelname)s", "message": "%(message)s"}'
        if json
        else "[%(levelname)s] %(asctime)s - %(name)s - %(message)s"
    )

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {"format": formatter},
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                }
            },
            "root": {
                "level": level,
                "handlers": ["console"],
            },
        }
    )
