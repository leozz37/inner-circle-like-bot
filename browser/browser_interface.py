import re


class BrowserInterface:
    """
    Interface for browser interaction
    """
    def open_url(self, url: str) -> None:
        """
        Open the given URL on the browser

        :param url: URL to be opened
        :type url: str
        """
        raise NotImplementedError("open_url not implemented")

    def url_validation(self, url: str) -> bool:
        """
        Validates if the URL is valid
        """
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return re.match(regex, url) is not None
