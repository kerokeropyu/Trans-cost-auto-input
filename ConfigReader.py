from configparser import ConfigParser

class ConfigReader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = ConfigParser()
        self.config.read(self.config_file_path)

    def get_setting(self, section, setting_name):
        try:
            return self.config.get(section, setting_name)
        except:
            return None