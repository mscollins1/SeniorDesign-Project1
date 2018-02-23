import jobPostingFromStackOverflow
import pytest


def test_user_exit():
    userInput = 'e'
    assert jobPostingFromStackOverflow.check_user_exit(userInput) is True

def test_user_continue():
    userInput = 'not e'
    assert jobPostingFromStackOverflow.check_user_exit(userInput) is False
