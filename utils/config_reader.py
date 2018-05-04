#!/usr/bin/env python3

import configparser


def get_mac_chrome_driver(base_path):
    config = configparser.ConfigParser()
    config.read(base_path + 'config/config.ini')
    return config['driver']['driver_path']