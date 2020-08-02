from jproperties import Properties


class FileIOUtils:

    @staticmethod
    def app_file_reader(property_name):
        configs = Properties()
        with open('application.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property_name)

    @staticmethod
    def endpoint_file_reader(property_name: str):
        configs = Properties()
        with open('endPoint.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property_name)

    @staticmethod
    def write_txt_file(filename, content: str, access_mode: str):
        f = open(filename, "w")
        f.write(content)
        f.close()

    @staticmethod
    def read_txt_file(filename: str):
        f = open(filename, "r")
        return f.read()
