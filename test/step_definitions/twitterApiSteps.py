import pytest
from pytest_bdd import scenario, given, when, then, parsers
from main.pages import twitterApiPage

scenario('../features/twitter.feature')


class TwitterSteps:
    twitterPg = twitterApiPage.Twitter()

    @given("A valid token is generated for a user")
    def loginapi(self):
        self.twitterPg.loginApi()

    @then(parsers.parse("Post a tweet with content {content}"))
    def tweet(content):
        pass

    @when("The previous tweet is retweeted")
    def retweet(self):
        pass

    @then("Fetch the retweet count and retweeters Ids")
    def fetchRetweetDetails(self):
        pass

    @given("The user revert the previous")
    def revertTweet(self):
        pass

    @then("delete the tweet")
    def deleteTweet(self):
        pass
