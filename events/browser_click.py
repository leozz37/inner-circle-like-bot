import pyautogui

from events.browser_events_interface import BrowserEventsInterface


class BrowserClick(BrowserEventsInterface):
    """
    This class interact with the web browser
    """

    def click_like(self) -> None:
        """
        Click the like button on Inner Circle page
        """

        # This resolution is based on my personal monitor
        pyautogui.click(1300, 533)

    def print_mouse_position(self):
        """
        Show in real time the mouse position coordinates
        """
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), end="", flush=True)
