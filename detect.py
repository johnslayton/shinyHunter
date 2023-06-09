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
image_window = "Source Image"
result_window = "Result window"

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
    wild = cv2.imread("images\\wild.png", 0)
    # img = cv2.imread(im)
    img_rgb = convert_from_image_to_cv2(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, wild, cv2.TM_CCOEFF_NORMED)
    w, h = wild.shape[::-1]
    # Specify a threshold
    threshold = 0.8
    
    # Store the coordinates of matched area in a numpy array
    loc = np.where(result >= threshold)
    # Draw a rectangle around the matched region.
    # print(loc)
    if len(loc) == 0:
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        
        # Show the final image with the matched area.
        cv2.imshow('Detected', img_rgb)

    # TODO: check that the found wild is in the correct area
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, max_val, min_loc, max_loc)
    # test=ImageGrab.grab(bbox=(387, 64, 565, 88))
    # test.show()
    # confidence = result
    # print(confidence)

    # img_display = img_rgb
    # matchLoc = min_loc
    # cv2.rectangle(img_display, matchLoc, (matchLoc[0] + wild.shape[0], matchLoc[1] + wild.shape[1]), (0,0,0), 2, 8, 0 )
    # cv2.rectangle(result, matchLoc, (matchLoc[0] + wild.shape[0], matchLoc[1] + wild.shape[1]), (0,0,0), 2, 8, 0 )
    # cv2.imshow(image_window, img_display)
    # cv2.imshow(result_window, result)
    cv2.waitKey(0)
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

