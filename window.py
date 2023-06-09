import win32gui


dims = [-1, -1]
windowName = "mGBA"

def callback(hwnd, extra):
    # if win32gui.GetWindowText(hwnd).__contains__
    if windowName in win32gui.GetWindowText(hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        # print("Window %s:" % win32gui.GetWindowText(hwnd))
        # print("\tLocation: (%d, %d)" % (x, y))
        # print("\t    Size: (%d, %d)" % (w, h))

        # resize for consistency
        win32gui.MoveWindow(hwnd, 0, 0, 1200, 800, True)
        global dims
        dims = [w,h]


def getDimensions():
    win32gui.EnumWindows(callback, None)
    return dims



