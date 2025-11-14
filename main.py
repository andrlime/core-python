from core.logger import LogLevel, get_logger
from core.pipe import Pipe

logger = get_logger(__name__, LogLevel.DEBUG)

if __name__ == "__main__":
    logger.debug("hello world")
    logger.warning("hello world")
    logger.info("hello world")
    logger.error("hello world")
    logger.critical("hello world")

    (
        Pipe((5, 7))
        >> (lambda u, v: (u + v, 2))
        >> (lambda x, y: x + 3 + y)
        >> (lambda x: x + 3)
        >> (lambda x: x + 3)
        >> (lambda x: x + 3)
        >> (lambda x: x + 3)
        >> (lambda x: x + 3)
        >> print
    )
