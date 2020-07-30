from jproperties import Properties


class FileIOUtils:

    def appFileReader(self, property_name):
        configs = Properties()
        with open('application.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property_name)

    def endpointFileReader(self, property_name: str):
        configs = Properties()
        with open('endPoint.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property_name)

    def writeTxtFile(self, filename, content: str):
        f = open(filename, "w")
        f.write(content)
        f.close()

    def readTxtFile(self, filename: str):
        f = open(filename, "r")
        return f.read()
