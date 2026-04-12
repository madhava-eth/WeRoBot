# -*- coding: utf-8 -*-
from bottle import request, HTTPResponse

import html


def make_view(robot):
    """
    为一个 BaseRoBot 生成 Bottle view。

    Usage ::

        from werobot import WeRoBot

        robot = WeRoBot(token='token')


        @robot.handler
        def hello(message):
            return 'Hello World!'

        from bottle import Bottle
        from werobot.contrib.bottle import make_view

        app = Bottle()
        app.route(
            '/robot',  # WeRoBot 挂载地址
            ['GET', 'POST'],
            make_view(robot)
        )


    :param robot: 一个 BaseRoBot 实例
    :return: 一个标准的 Bottle view
    """
    def werobot_view(*args, **kwargs):
        pass

    return werobot_view
