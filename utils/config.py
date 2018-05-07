#!/usr/bin/env python3

import configparser
import os
import sys


class Config(object):

    __base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    __config = configparser.ConfigParser().read(
        os.path.join(__base_path, 'config', 'config.ini'))

    @classmethod
    def get_mac_chrome_driver(cls):
        return cls.__config['mac']['chrome_driver_path']

    @classmethod
    def get_win_chrome_driver(cls):
        return cls.__config['win']['chrome_driver_path']
    
    @classmethod
    def get_log_path(cls):
        return os.path.join(cls.__base_path, 'log')
