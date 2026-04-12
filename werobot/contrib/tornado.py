# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

import html


def make_handler(robot):
    """
    为一个 BaseRoBot 生成 Tornado Handler。

    Usage ::

        import tornado.ioloop
        import tornado.web
        from werobot import WeRoBot
        from tornado_werobot import make_handler

        robot = WeRoBot(token='token')


        @robot.handler
        def hello(message):
            return 'Hello World!'

        application = tornado.web.Application([
            (r"/", make_handler(robot)),
        ])

    :param robot: 一个 BaseRoBot 实例。
    :return: 一个标准的 Tornado Handler
    """
    pass
