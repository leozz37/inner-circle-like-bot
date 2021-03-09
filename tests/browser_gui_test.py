import pytest

from browser.browser_gui import BrowserGUI


@pytest.fixture
def browser_gui() -> BrowserGUI:
    """
    Create an instance to be used across the test suite
    """
    browser_guir = BrowserGUI()

    yield browser_gui


@pytest.mark.skip("WIP")
def test_open_url_with_success(browser_gui: BrowserGUI) -> None:
    """
    Test if the URL is opened
    """
    assert True
