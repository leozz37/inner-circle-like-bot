import webbrowser

from browser.browser_interface import BrowserInterface


class BrowserGUI(BrowserInterface):
    """
    This class interact with the web browser
    """

    def open_url(self, url: str) -> bool:
        """
        Open the given URL on the browser

        :param url: URL to be opened
        :type url: str

        :return: True if succeed
        :rtype: bool
        """
        if self.validate_url(url):
            webbrowser.open(url, new=2)
            return True
        else:
            return False
