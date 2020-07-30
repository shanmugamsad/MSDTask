import requests
from jproperties import Properties
from main.utils.FileIOUtils import FileIOUtils
import base64


class Twitter:
    fileReadWrite = FileIOUtils()
    ipUrl = fileReadWrite.appFileReader('apiUrl')

    def login_api(self):
        endpoint = FileIOUtils.endpointFileReader('login')
        param = {"grant_type": "client_credentials"}
        header = {"Authorization": base64.b16decode(
            self.fileReadWrite.appFileReader("consumerKey") + ':' + self.fileReadWrite.appFileReader("secretKey"))}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 200:
            data = response.json()
            self.fileReadWrite.writeTxtFile('token', data['access_token'])

    def post_tweet(self, content):
        endpoint = FileIOUtils.endpointFileReader('tweet')
        param = {"status": content}
        header = {"Authorization": "Bearer " + self.fileReadWrite.readTxtFile('token')}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 201:
            data = response.json()
            self.fileReadWrite.writeTxtFile('tweetId', data['id'])
            assert str(data['text']) == content

    def re_tweet(self):
        endpoint = str(FileIOUtils.endpointFileReader('re_tweet')).replace('{id}',FileIOUtils.readTxtFile('tweetId'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.readTxtFile('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched

    def un_re_tweet(self):
        endpoint = str(FileIOUtils.endpointFileReader('un_re_tweet')).replace('{id}', FileIOUtils.readTxtFile('tweetId'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.readTxtFile('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched

    def delete_tweet(self):
        endpoint = str(FileIOUtils.endpointFileReader('delete_tweet')).replace('{id}', FileIOUtils.readTxtFile('tweetId'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.readTxtFile('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched
