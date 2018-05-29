import configparser
import os
# from utils.log import logger


__base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# __ini = os.environ.get('WEBUI_SETTINGS_INI')
__default_ini = "default_config.ini"
__config = configparser.ConfigParser()
__config.read(os.path.join(__base_path, 'config', __default_ini))

LOG_PATH = os.path.join(__base_path, 'log')

URL = __config.get('url', 'url')

__env_dist = os.environ

if "BROWSER_VENDOR" in __env_dist:
    BROWSER_VENDOR = __env_dist['BROWSER_VENDOR']
    # logger.info("BROWSER_VENDOR is found in System environment variables")
    # logger.info("BROWSER_VENDOR is set to: " + BROWSER_VENDOR)
else:
    BROWSER_VENDOR = __config.get('DEFAULT', 'BROWSER_VENDOR')
    # logger.info("BROWSER_VENDOR is Not found in System environment variables, default value is used")
    # logger.info("BROWSER_VENDOR is set to: " + BROWSER_VENDOR)

if "BROWSER_DRIVER" in __env_dist:
    BROWSER_DRIVER = __env_dist['BROWSER_DRIVER']
    # logger.info("BROWSER_DRIVER is found in System environment variables")
    # logger.info("BROWSER_DRIVER is set to: " + BROWSER_DRIVER)
else:
    BROWSER_DRIVER = __config.get('DEFAULT', 'BROWSER_DRIVER')
    # logger.info("BROWSER_DRIVER is Not found in System environment variables, default value is used")
    # logger.info("BROWSER_DRIVER is set to: " + BROWSER_DRIVER)
