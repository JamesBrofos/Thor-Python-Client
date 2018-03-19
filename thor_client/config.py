import configparser
import os


config = configparser.ConfigParser()
config.read(['config.ini', os.path.expanduser('~/.thorconfig.ini')],
            encoding='utf8')

base_url = str(os.environ.get('THOR_BASE_URL', config['thor']['base_url']))
auth_token = str(os.environ.get('THOR_AUTH_TOKEN', config['thor']['auth_token']))
