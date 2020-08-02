from behave import *
from main.services import twitter_services
from main.utils.FileIOUtils import FileIOUtils


twitterPg = twitter_services.Twitter()
file_read_write: FileIOUtils = FileIOUtils()


@given(u'Tweet content is fetched for "{tweet_id}"')
def step_impl(tweet_id):
    twitterPg.fetch_tweet(tweet_id)


@then('Download the video in the same tweet with "{tweet_id}"')
def step_impl(tweet_id):
    twitterPg.fetch_tweet(tweet_id)


@then('Fetch the re_tweet count and re_tweeters Ids for the same tweet with "{tweet_id}"')
def step_impl(tweet_id):
    twitterPg.fetch_retweet_count(tweet_id)
    twitterPg.fetch_reweeters_ids(tweet_id)


@then('Verify the Tweet content for "{tweet_id}"')
def get_tweet_content(self, tweet_id):
    self.twitterPg.tweet(tweet_id)


@given('A valid token is generated for a user')
def login_api(self):
    self.twitterPg.login_api()


@then("Post a tweet with content <content>")
def tweet(self, content):
    self.twitterPg.tweet(content)


@when("The previous tweet is re_tweeted")
def re_tweet(self):
    if not file_read_write.readTxtFile('tweet_id'):
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
