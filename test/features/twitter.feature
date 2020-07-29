Feature: Twitter API
  Login to Twitter and Create a Tweet, Retweet it and Untweet the same

 Scenario Outline: Login and post a tweet
    Given A valid token is generated for a user
    Then post a tweet with content "<content>"

   Examples:
   |content|
   |We welcome you to MSD family :)|