# -*- coding: utf-8 -*-
# @Time     : 2020/7/22 14:23
# @Author   : Zhili
# @FileName : conftest.py
# @Software : PyCharm
import time

import pytest
import yaml
import os
from appium import webdriver
from HooAppUIProject.Common.get_path import caps_dir
from HooAppUIProject.Common.input_code import input_code
from HooAppUIProject.PageObjects.HomePage.home_page_objects import HomePage
from HooAppUIProject.PageObjects.LoginRegisterPageObjects.login_register_page_objects import LoginRegisterPage
import logging
from HooAppUIProject.Common.get_data import GetData


@pytest.fixture
def start_app():
    # 启动会话设置noReset=True,启动不重置
    driver = base_driver(noReset=True)
    yield driver
    driver.close()
    driver.quit()


# 启动会话设置noReset=True,启动不重置
@pytest.fixture(scope="class")
def base_driver(noReset=True, automationName=None, server_port=4723):
    # 读取全局的一个caps选项。
    fs = open(os.path.join(caps_dir, "caps.yaml"))
    desired_caps = yaml.load(fs)
    # 根据参数来定制化启动选项
    if noReset is not None and noReset in [True, False]:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName
    # 启动浏览器会话,与appium server进行连接，并发送要操作的设备对象信息。
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(server_port), desired_caps)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="class")
def is_logined(noReset=True, automationName=None, server_port=4723):
    # 读取全局的一个caps选项。
    fs = open(os.path.join(caps_dir, "caps.yaml"))
    desired_caps = yaml.load(fs)
    # 根据参数来定制化启动选项
    if noReset is not None and noReset in [True, False]:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName
    # 启动浏览器会话,与appium server进行连接，并发送要操作的设备对象信息。
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(server_port), desired_caps)
    if not HomePage(driver).is_loginRegisterBtn_exist():
        logging.debug("当前尚未登陆状态")
        HomePage(driver).click_LoginRegister_Btn()
        LoginRegisterPage(driver).input_tel_box(GetData().get_login_tel())
        LoginRegisterPage(driver).input_password_box(GetData().get_login_pwd())
        LoginRegisterPage(driver).click_agree_box()
        LoginRegisterPage(driver).click_login_btn()
        time.sleep(3)
        input_code(driver, GetData().get_vcode())
    else:
        logging.debug("当前用户已登陆")
    yield driver
    driver.close()
    driver.quit()


#
#
# # 欢迎页面处理
# def swipe_welcome(driver):
#     time.sleep(6)
#     # 判断是否在欢迎页面
#     activity = driver.current_activity
#     # 首页名称不在当前的活动页面名称中
#     if "MainActivity" not in activity:
#         print("当前为欢迎页面")
#         # 欢迎页面的滑屏操作。
#         # 如果在欢迎页面，我就向左滑三次
#         size = driver.get_window_size()
#         for index in range(0, 3):
#             driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5)
#             time.sleep(1)
#         # 点击“立即体验”
#         time.sleep(1)
#         driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()

# # 登陆用例 - toast会话
# def start_app_toast():
#     # 启动会话  需要["automationName"] = "UiAutomator2"
#     driver = base_driver(automationName="UiAutomator2")
#     # 判断一下，当前的页面是首页还是欢迎页面
#     # 如果是欢迎页面，那我就滑屏操作。
#     swipe_welcome(driver)
#     yield driver
#     driver.close_app()
#     driver.quit()

#
# 通用前置 后置

@pytest.fixture(scope='class')
def startApp_keepUserData():
    # 打开app，不重置
    driver = base_driver(noReset=True)
    # 欢迎页面处理
    # swipe_welcome(driver)
    # 是否是已登陆状态  #个人页面  #首页
    # is_logined(driver)
    # yield driver
    # driver.close_app()
    # driver.quit()
