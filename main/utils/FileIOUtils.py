from jproperties import Properties


class FileIOUtils:

    def appFileReader(self,property):
        configs = Properties()
        with open('application.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property)

    def endpointFileReader(self,property):
        configs = Properties()
        with open('endPoint.properties', 'rb') as config_file:
            configs.load(config_file)
        return configs.get(property)

    def writeTxtFile(self,fileName,content):
        f = open(fileName, "w")
        f.write(content)
        f.close()

    def readTxtFile(self,fileName):
        f = open(fileName, "r")
        return f.read()