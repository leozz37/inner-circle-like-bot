import time
import os

from browser.browser_gui import BrowserGUI
from events.browser_click import BrowserClick


# Debug mode outputs to stdout detailed information about each line processed
DEBUG_MODE = os.environ["APP_DEBUG_MODE"]   # pragma: no cover

if __name__ == '__main__':  # pragma: no cover
    """
    Main program entrypoint
    """
    if DEBUG_MODE == "True":
        print("DEBUG: Debug mode enabled")
        print("Press Ctrl-C to quit.")

    try:
        inner_circle_url = "https://theinnercircle.co/"
        browser = BrowserGUI()
        # TODO: implement validation
        browser.open_url(inner_circle_url)

        browser_click = BrowserClick()

        while True:
            if DEBUG_MODE == "True":
                browser_click.print_mouse_position()
            browser_click.click_like()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nDone.")

