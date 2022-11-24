from configparser import ConfigParser

config=ConfigParser()
print(config)
config['DEFAULT']={
    'login': 'mylogin',
    'pass': 'mypass'
}

config['EMAIL']={
    'email':'roman@com',
    'email_pass':'1234'
}

config['DATABASE']={
    'name':'db_root',
    'user':'root',
    'pass':'1234',
    'host':'hostename'
}

with open("config,ini",'w')as config_file:
    config.write(config_file)