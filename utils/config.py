import configparser
import os


__base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# __ini = os.environ.get('WEBUI_SETTINGS_INI')
__ini = "default_config.ini"
__config = configparser.ConfigParser()
__config.read(os.path.join(__base_path, 'config', __ini))

LOG_PATH = os.path.join(__base_path, 'log')

URL = __config.get('url', 'url')

__env_dist = os.environ

if "browser.vendor" in __env_dist:
    BROWSER_VENDOR = __env_dist['browser.vendor']
else:
    BROWSER_VENDOR = __config.get('DEFAULT', 'browser.vendor')

if "browser.driver" in __env_dist:
    BROWSER_DRIVER = __env_dist['browser.driver']
else:
    BROWSER_DRIVER = __config.get('DEFAULT', 'browser.driver')