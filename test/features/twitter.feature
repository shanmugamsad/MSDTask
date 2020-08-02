Feature: Twitter API
  Login to Twitter and Create a Tweet, Retweet it and Untweet the same

  @task1
  Scenario Outline: Login and post a tweet
    Given Tweet content is fetched for <tweet_id>
    Then Download the video in the same tweet with <tweet_id>
    Then Fetch the re_tweet count and re_tweeters Ids for the same tweet with <tweet_id>

   Examples:
   |tweet_id|
   |1257326183101980673|

  @task1
  Scenario Outline: Re_tweet and fetch id and count of re_tweets
    Then Verify the Tweet content for <tweet_id>
    Then Verify the re_tweet count for <tweet_id>
    Then Verify the re_tweeters Ids for the same tweet with <tweet_id>

    Examples: Vertical
      | tweet_id            |
      | 1257326183101980673 |

  @task2
  Scenario Outline: Login and post a tweet
    Given A valid token is generated for a user
    Then Post a tweet with content <content>

   Examples:
   |content|
   |We welcome you to MSD family :)|

  @task2
  Scenario: Re_tweet and fetch id and count of re_tweets
    When The previous tweet is re_tweeted
    Then Fetch the re_tweet count and re_tweeters Ids

  @task2
  Scenario: Un_re_tweet and Delete the tweet
    Given The user revert the previous
    Then Fetch the re_tweet count and re_tweeters Ids
    Then delete the tweet
