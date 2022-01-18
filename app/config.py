import os, urllib.parse
class Config(object):
    TEST_ENV_VAR1: str = os.environ.get('TEST_ENV_VAR1')
    TEST_ENV_VAR2: str = os.environ.get('TEST_ENV_VAR2')





