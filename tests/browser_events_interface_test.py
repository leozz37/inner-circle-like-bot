import pytest

from events.browser_events_interface import BrowserEventsInterface


@pytest.fixture()
def be() -> BrowserEventsInterface:
    """
    Create a instance to be used across the test suite
    """
    # Set up
    be = BrowserEventsInterface()

    yield be


def test_click_like_implementation(be: BrowserEventsInterface) -> None:
    """
    Test if open_url is implemented
    """
    expected_output = "click_like not implemented"

    with pytest.raises(Exception) as e:
        assert be.click_like()

    assert expected_output in str(e)
