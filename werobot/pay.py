# -*- coding:utf-8 -*-

from hashlib import sha1, md5
from urllib import urlencode
import time
from werobot.client import Client
from werobot.utils import pay_sign_dict, generate_token
from functools import partial

NATIVE_BASE_URL = 'weixin://wxpay/bizpayurl?'


class WeixinPayClient(Client):
    """
    简化微信支付API操作
    """
    def __init__(self, appid, pay_sign_key, pay_partner_id, pay_partner_key):
        self.pay_sign_key = pay_sign_key
        self.pay_partner_id = pay_partner_id
        self.pay_partner_key = pay_partner_key
        self._pay_sign_dict = partial(pay_sign_dict, appid, pay_sign_key)

        self._token = None
        self.token_expires_at = None

    def create_js_pay_package(self, **package):
        """
        签名 pay package 需要的参数
        详情请参考 支付开发文档

        :param package: 需要签名的的参数
        :return: 可以使用的packagestr
        """
        pass

    def create_js_pay_params(self, **package):
        """
        签名 js 需要的参数
        详情请参考 支付开发文档

        ::

            wxclient.create_js_pay_params(
                body=标题, out_trade_no=本地订单号, total_fee=价格单位分,
                notify_url=通知url,
                spbill_create_ip=建议为支付人ip,
            )

        :param package: 需要签名的的参数
        :return: 支付需要的对象
        """
        pass

    def create_js_edit_address_param(self, accesstoken, **params):
        """
        alpha
        暂时不建议使用
        这个接口使用起来十分不友好
        而且会引起巨大的误解

        url 需要带上 code 和 state (url?code=xxx&state=1)
        code 和state 是 oauth 时候回来的

        token 要传用户的 token

        这尼玛 你能相信这些支付接口都是腾讯出的？
        """
        pass

    def create_native_pay_url(self, productid):
        """
        创建 native pay url
        详情请参考 支付开发文档

        :param productid: 本地商品ID
        :return: 返回URL
        """
        pass

    def pay_deliver_notify(self, **deliver_info):
        """
        通知 腾讯发货

        一般形式 ::
            wxclient.pay_delivernotify(
                openid=openid,
                transid=transaction_id,
                out_trade_no=本地订单号,
                deliver_timestamp=int(time.time()),
                deliver_status="1",
                deliver_msg="ok"
            )

        :param 需要签名的的参数
        :return: 支付需要的对象
        """
        pass

    def pay_order_query(self, out_trade_no):
        """
        查询订单状态
        一般用于无法确定 订单状态时候补偿

        :param out_trade_no: 本地订单号
        :return: 订单信息dict
        """
        pass
