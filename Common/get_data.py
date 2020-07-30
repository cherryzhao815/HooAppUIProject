# -*- coding: utf-8 -*-
# @Time     : 2020/7/30 13:54
# @Author   : Zhili
# @FileName : get_data.py
# @Software : PyCharm
from HooAppUIProject.Common.read_config import ReadConfig
from HooAppUIProject.Common import get_path


class GetData:

    # TradePwd = ReadConfig.get_config(get_path.config_dir, 'basic_info', 'TradePwd')
    # getattr(GetData, 'TradePwd')

    # 获取url
    def get_host_url(self):
        host_url = ReadConfig.get_config(get_path.config_dir, 'basic_info', 'HostURL')
        return host_url

    # 获取登录用户名
    def get_login_tel(self):
        login_tel = ReadConfig.get_config(get_path.config_dir, 'basic_info', 'LoginTel')
        return login_tel

    # 获取登录密码
    def get_login_pwd(self):
        login_pwd = ReadConfig.get_config(get_path.config_dir, 'basic_info', 'LoginTel')
        return login_pwd

    # 获取验证码
    def get_vcode(self):
        vcode = ReadConfig.get_config(get_path.config_dir, "basic_info", "vcode")
        return vcode

    # 获取交易密码
    def get_trade_pwd(self):
        trade_pwd = ReadConfig.get_config(get_path.config_dir, 'basic_info', 'TradePwd')
        return trade_pwd
