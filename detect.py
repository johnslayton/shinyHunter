# detection
import cv2
from matplotlib import pyplot as plt
from PIL import ImageGrab, Image
import numpy as np
# Pressed at (46, 789)
# Released at (46, 789)
# Pressed at (1154, 52)
# Released at (1154, 52)
#
coords = [45, 52, 1155, 790]


def convert_from_cv2_to_image(img: np.ndarray) -> Image:
    # return Image.fromarray(img)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    # return np.asarray(img)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def detect():
    # take screenshot
    print("detect")
    # win32gui.MoveWindow(hwnd, 0, 800, 0, 1200, True)
    im=ImageGrab.grab(bbox=(coords[0],coords[1],coords[2],coords[3]))
    # im.show()
    wild = cv2.imread("images\\wild.png")
    # img = cv2.imread(im)
    img = convert_from_image_to_cv2(im)
    img.show()
    # img_gray = cv2.cvtColor(convert_from_image_to_cv2(im), cv2.COLOR_BGR2GRAY)
    # img_rgb = cv2.cvtColor(convert_from_image_to_cv2(im), cv2.COLOR_BGR2RGB)
    # img_rgb.show()
    # plt.subplot(1, 1, 1)
    # plt.imshow(img_rgb)
    # plt.show()
    #got image

detect()

def saveClipboard():
    im = ImageGrab.grabclipboard()
    # im.show()
    im.save('images\\wild.png')

