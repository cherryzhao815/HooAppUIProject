# _*_coding:utf-8_*_
# author: zhili.zhao
# time: 2019/4/17 16:07
# file name: read_config.py
# IDE: PyCharm
import configparser


class ReadConfig:

    @staticmethod
    def get_config(file_path, section, option):
        """
        :param file_path: 配置文件的路径+名称
        :param section: 配置文件中的MODE
        :param option: 配置文件中的选项
        :return: option中的值
        """
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


