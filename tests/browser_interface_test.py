import pytest

from browser.browser_interface import BrowserInterface


@pytest.fixture()
def bi() -> BrowserInterface:
    """
    Create a instance to be used across the test suite
    """
    # Set up
    bi = BrowserInterface()

    yield bi


def test_open_url_implementation(bi: BrowserInterface) -> None:
    """
    Test if open_url is implemented
    """
    expected_output = "open_url not implemented"

    with pytest.raises(Exception) as e:
        assert bi.open_url("empty url")

    assert expected_output in str(e)


def test_url_validation_with_success(bi: BrowserInterface) -> None:
    """
    Test if the url is valid
    """
    url = "http://www.example.com"
    assert bi.validate_url(url)

    url = "https://www.example.com"
    assert bi.validate_url(url)

    url = "https://www.example.com.br"
    assert bi.validate_url(url)


def test_url_validation_fails(bi: BrowserInterface) -> None:
    """
    Test if the url is not valid
    """
    url = "www.example.com"
    assert not bi.validate_url(url)

    url = "https:www.localhost"
    assert not bi.validate_url(url)
