from my_bindu_agent.main import handler


def test_handler():
    """Test that handler accepts messages and returns a RunOutput."""
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    result = handler(messages)

    # Check that we get a result back
    assert result is not None

    # Check that the result has expected attributes from agno RunOutput
    assert hasattr(result, "run_id")
    assert hasattr(result, "status")
