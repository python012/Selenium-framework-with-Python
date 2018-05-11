#!/usr/bin/env python3

import configparser
import os


__base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
__config = configparser.ConfigParser()
__config.read(os.path.join(__base_path, 'config', 'config.ini'))


def get_mac_chrome_driver():
    return __config.get('mac', 'chrome_driver_path')


def get_win_chrome_driver():
    return __config.get('win', 'chrome_driver_path')


def get_log_path():
    return os.path.join(__base_path, 'log')
    

def get_url():
    return __config.get('url', 'url')


