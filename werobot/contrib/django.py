# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import html


def make_view(robot):
    """
    为一个 BaseRoBot 生成 Django view。

    :param robot: 一个 BaseRoBot 实例。
    :return: 一个标准的 Django view
    """
    @csrf_exempt
    def werobot_view(request):
        pass

    return werobot_view
