from pytest_bdd import scenario, given, when, then, parsers
from main.services import twitterApiPage
from main.utils.FileIOUtils import FileIOUtils


@scenario('../features/twitter.feature')
def test_twitter():
    pass


twitterPg = twitterApiPage.Twitter()
file_read_write: FileIOUtils = FileIOUtils()


@given("A valid token is generated for a user")
def login_api(self):
    self.twitterPg.login_api()


@then(parsers.parse("Post a tweet with content <content>"))
def tweet(self, content):
    self.twitterPg.tweet(content)


@when("The previous tweet is re_tweeted")
def re_tweet(self):
    if not file_read_write.readTxtFile('tweetId'):
        self.twitterPg.post_tweet()
    else:
        print('Tweet was not posted to re_tweet')


@then("Fetch the re_tweet count and re_tweeters Ids")
def fetch_re_tweet_details(self):
    pass


@given("The user revert the previous")
def revert_tweet(self):
    pass


@then("delete the tweet")
def delete_tweet(self):
    pass
