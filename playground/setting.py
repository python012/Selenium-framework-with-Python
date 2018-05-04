#!/usr/bin/env python3

from conf import global_settings


class Settings(object):

    def __init__(self):
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))

if __name__ == "__main__":
    s = Settings()
    for attr in dir(s):
        if attr.isupper():
            print(attr + " - " + s.__getattribute__(attr))

