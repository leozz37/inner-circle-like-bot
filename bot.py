import pyautogui
import webbrowser
import time

print('Press Ctrl-C to quit.')
webbrowser.open("https://theinnercircle.co/", new=2)

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        pyautogui.click(1300, 533)
        time.sleep(1)

except KeyboardInterrupt:
    print('\nDone.')
