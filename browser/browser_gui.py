import webbrowser

from browser.browser_interface import BrowserInterface


class BrowserGUI(BrowserInterface):
    """
    This class interact with the web browser
    """

    def open_url(self, url: str) -> None:
        """
        Open the given URL on the browser

        :param url: URL to be opened
        :type url: str
        """
        webbrowser.open(url, new=2)
