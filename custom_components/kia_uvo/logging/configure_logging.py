import logging
import logging.config
import yaml

with open("logging_config.yaml", 'r') as the_file:
    config_dict = yaml.load(the_file)

logging.config.dictConfig(config_dict)
