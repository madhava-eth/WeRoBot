# -*- coding:utf-8 -*-

import sys
import time
import logging

try:
    import curses

    assert curses
except ImportError:
    curses = None

logger = logging.getLogger("WeRoBot")


def enable_pretty_logging(logger, level='info'):
    """
    按照配置开启 log 的格式化优化。

    :param logger: 配置的 logger 对象
    :param level: 要为 logger 设置的等级
    """
    pass


class _LogFormatter(logging.Formatter):
    def __init__(self, color, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)
        self._color = color
        if color:
            fg_color = (
                curses.tigetstr("setaf") or curses.tigetstr("setf") or b""
            )
            self._colors = {
                logging.DEBUG: str(curses.tparm(fg_color, 4), "ascii"),  # Blue
                logging.INFO: str(curses.tparm(fg_color, 2), "ascii"),  # Green
                logging.WARNING: str(curses.tparm(fg_color, 3),
                                     "ascii"),  # Yellow
                logging.ERROR: str(curses.tparm(fg_color, 1), "ascii"),  # Red
            }
            self._normal = str(curses.tigetstr("sgr0"), "ascii")

    def format(self, record):
        pass
