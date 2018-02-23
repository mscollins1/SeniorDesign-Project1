import pytest
import jobPostingFromStackOverflow

def test_good_url():
    assert jobPostingFromStackOverflow.get_website_response("https://stackoverflow.com/jobs/feed?l=Bridgewater%2c+MA%2c+USA&u=Miles&d=50") is not None

def test_bad_url():
    assert jobPostingFromStackOverflow.get_website_response("httdps://stackoberqlow.com/jobs/feed?l=Bridgewater%2c+MA%2c+USA&u=Miles&d=50") is not None

