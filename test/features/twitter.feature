Feature: Twitter API
  Login to Twitter and Create a Tweet, Retweet it and Untweet the same

 Scenario Outline: Login and post a tweet
    Given A valid token is generated for a user
    Then Post a tweet with content <content>

   Examples: Vertical
   |content|
   |We welcome you to MSD family :)|

  Scenario: Re_tweet and fetch id and count of re_tweets
    When The previous tweet is re_tweeted
    Then Fetch the re_tweet count and re_tweeters Ids

  Scenario: Un_re_tweet and Delete the tweet
    Given The user revert the previous
    Then Fetch the re_tweet count and re_tweeters Ids
    Then delete the tweet
