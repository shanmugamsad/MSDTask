Feature: Twitter API
  Login to Twitter and Create a Tweet, Retweet it and Untweet the same

 Scenario Outline: Login and post a tweet
    Given A valid token is generated for a user
    Then Post a tweet with content "<content>"

   Examples:
   |content|
   |We welcome you to MSD family :)|

  Scenario: Retweet and fetch id and count of retweets
    When The previous tweet is retweeted
    Then Fetch the retweet count and retweeters Ids

  Scenario: Unretweet and Delete the tweet
    Given The user revert the previous
    Then Fetch the retweet count and retweeters Ids
    Then delete the tweet
