from pytest_bdd import scenario, given, when, then
from main.pages import twitterApiPage


@given("A valid token is generated for a user")
def loginapi():
    twitterPg = twitterApiPage.Twitter()
    twitterPg.loginApi()
