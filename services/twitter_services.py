import requests
from utilities.FileIOUtils import FileIOUtils
import base64


class Twitter:
    fileReadWrite = FileIOUtils()
    ipUrl = fileReadWrite.app_file_reader('apiUrl')

    def fetch_tweet(self, tweet_id):
        tweet_text = self.fetch_tweet_response(tweet_id)
        self.fileReadWrite.write_txt_file('tweet_data', tweet_text['text']+'#', 'a')

    def fetch_retweet_count(self, tweet_id):
        tweet_count = self.fetch_retweet_count_response(tweet_id)
        self.fileReadWrite.write_txt_file('tweet_data', tweet_count['retweet_count']+'#', 'a')

    def fetch_reweeters_ids(self, tweet_id):
        id_str = self.fetch_retweeters_id_response(tweet_id)
        self.fileReadWrite.write_txt_file('tweet_data', id_str, 'a')

    def verify_tweet_content(self,tweet_id):
        tweet_content = str(self.fileReadWrite.read_txt_file('tweet_data'))
        tweet_data_list = tweet_content.split("#")
        assert tweet_data_list[0]==self.fetch_tweet_response(tweet_id)['text']
        assert tweet_data_list[1] == self.fetch_retweet_count_response(tweet_id)['retweet_count']
        assert tweet_data_list[2] == self.fetch_retweeters_id_response(tweet_id)['text'].join(',')

    def fetch_tweet_response(self,tweet_id):
        endpoint = FileIOUtils.endpoint_file_reader('fetch_tweet')
        param = {"id": tweet_id}
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 200:
            tweet_text = response.json()
            return tweet_text

    def fetch_retweet_count_response(self,tweet_id):
        endpoint = str(FileIOUtils.endpoint_file_reader('re_tweet_count')).replace('{id}',
                                                                                   FileIOUtils.read_txt_file(tweet_id))
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200:
            tweet_count = response.json()
            return tweet_count

    def fetch_retweeters_id_response(self,tweet_id):
        endpoint = str(FileIOUtils.endpoint_file_reader('re_tweet_count')).replace('{id}',
                                                                                   FileIOUtils.read_txt_file(tweet_id))
        param = {"id": tweet_id, "stringify_ids": True}
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 200:
            data = response.json()
            ids_list = data['ids']
            id_str = ','.join(ids_list)
            return id_str

    def login_api(self):
        endpoint = FileIOUtils.endpoint_file_reader('login')
        param = {"grant_type": "client_credentials"}
        header = {"Authorization": base64.b16decode(
            self.fileReadWrite.app_file_reader("consumerKey") + ':' + self.fileReadWrite.app_file_reader("secretKey"))}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 200:
            data = response.json()
            self.fileReadWrite.write_txt_file('token', data['access_token'], 'r+')

    def post_tweet(self, content):
        endpoint = FileIOUtils.endpoint_file_reader('tweet')
        param = {"status": content}
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, params=param, headers=header)
        if response.status_code == 201:
            data = response.json()
            self.fileReadWrite.write_txt_file('tweet_id', data['id'], 'r+')
            assert str(data['text']) == content

    def re_tweet(self):
        endpoint = str(FileIOUtils.endpoint_file_reader('re_tweet')).replace('{id}',
                                                                             FileIOUtils.read_txt_file('tweet_id'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched

    def un_re_tweet(self):
        endpoint = str(FileIOUtils.endpoint_file_reader('un_re_tweet')).replace('{id}',
                                                                                FileIOUtils.read_txt_file('tweet_id'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched

    def delete_tweet(self):
        endpoint = str(FileIOUtils.endpoint_file_reader('delete_tweet')).replace('{id}',
                                                                                 FileIOUtils.read_txt_file('tweet_id'))
        header = {"Authorization": "Bearer " + self.fileReadWrite.read_txt_file('token')}
        response = requests.post(url=self.ipUrl + endpoint, headers=header)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # T0-Do when response is fetched
