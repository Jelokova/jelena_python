from configparser import ConfigParser

use_setting = 'DATABASE'
config = ConfigParser()

config.read('config.ini')
# print(config[use_setting]['login'])
# print(dict(config['EMAIL']))

config.add_section('NEW_SECTION')
config.set('NEW_SECTION','login','roman')
config.set('NEW_SECTION','pass','11112')
print(config['NEW_SECTION'],['login'])