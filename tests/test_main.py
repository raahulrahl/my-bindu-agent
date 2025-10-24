from my_bindu_agent.main import handler


def test_handler():
    assert handler("foo") == "foo"
