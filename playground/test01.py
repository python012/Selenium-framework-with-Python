#!/usr/bin/env python3

import os
import sys

base_path = None
if os.name == 'nt':
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\\..\\'
else:
    base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

sys.path.append(base_path)


from utils.config_reader import ConfigReader


print(ConfigReader(base_path).get_win_chrome_driver())
