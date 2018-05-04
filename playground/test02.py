#!/usr/bin/env python3

import configparser
import os
import sys

class ConfigReader(object):

    def __init__(self, base_path):
        self.__config_path = os.path.join(base_path, 'config', 'config.ini')
        if os.path.exists(self.__config_path):
            self.config = configparser.ConfigParser()
            self.config.read(self.__config_path)
        else:
            raise FileNotFoundError(
                'Config file is NOT present as "' + self.__config_path + '" !')

    def get_mac_chrome_driver(self):
        return self.config['mac']['chrome_driver_path']

    def get_win_chrome_driver(self):
        return self.config['win']['chrome_driver_path']
