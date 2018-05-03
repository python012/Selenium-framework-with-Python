#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
driver_path = config['dirver']['driver_path']

# print(driver_path)