import requests
from jproperties import Properties
from main.utils.FileIOUtils import FileIOUtils


class Twitter:
    fileReadWrite = FileIOUtils()
    ipUrl = fileReadWrite.appFileReader('apiUrl')

    def loginApi(self):
        endpoint = FileIOUtils.endpointFileReader('login')
        response = requests.get(self.ipUrl + endpoint)
        if response.status_code == 200:
            data = response.json()
            self.fileReadWrite.writeTxtFile('token.txt',data['access_token'])
