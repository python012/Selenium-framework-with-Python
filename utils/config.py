import configparser
import os


__base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
__ini = os.environ.get('WEBUI_SETTINGS_INI')
__config = configparser.ConfigParser()
__config.read(os.path.join(__base_path, 'config', __ini))

FIREFOX_DRIVER_PATH = __config.get('mac', 'chrome_driver_path')

LOG_PATH = os.path.join(__base_path, 'log')

URL = __config.get('url', 'url')
