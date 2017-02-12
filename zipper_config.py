import json
import errno

config = {
    'first_file_filesize'   : '1024',
    'second_file_filesize'  : '128'
}

def write_config():
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def read_config():
    try:
        config_file = open('config.json', 'r')
        config = json.load(config_file)        
    except Exception as error:
        if errno.ENOENT == error.errno:
            #config file doesn't exist, create one with defaults
            write_config()
