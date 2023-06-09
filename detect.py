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

def detect_shiny():
    print("asdf")


def detect_wild():
    # take screenshot
    im=ImageGrab.grab(bbox=(coords[0],coords[1],coords[2],coords[3]))
    # im.show()
    # template
    wild = cv2.imread("images\\wild.png", 0)

    # convert to cv2 for matching
    img_rgb = convert_from_image_to_cv2(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, wild, cv2.TM_CCOEFF_NORMED)
    # dimensions of template
    w, h = wild.shape[::-1]

    # Specify a threshold
    threshold = 0.8
    # Store the coordinates of matched area in a numpy array
    loc = np.where(result >= threshold)
    # Draw a rectangle around the matched region.
    # flag for if wild was found
    flag = False
    for pt in zip(*loc[::-1]):
        flag = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        # Show the final image with the matched area.

    # if flag:
    # print('wild pokemon appeared')
    # cv2.imshow('Detected', img_rgb)
    # cv2.waitKey(0)
    return flag


def detect_template(template):

    grab = ImageGrab.grab(bbox=(0,0, 1200, 800))
    source_image = convert_from_image_to_cv2(grab)
    template_image = cv2.imread("images\\" + template + ".png")
    source_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)
    template_hsv = cv2.cvtColor(template_image, cv2.COLOR_BGR2HSV)

    # Extract the Hue channel
    source_hue = source_hsv[:,:,0]
    template_hue = template_hsv[:,:,0]

    # Perform template matching
    result = cv2.matchTemplate(source_hue, template_hue, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the top-left and bottom-right corners of the matched region
    template_width, template_height = template_hue.shape[::-1]
    top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

    # Draw a bounding box around the detected match
    cv2.rectangle(source_image, top_left, bottom_right, (0, 255, 255), 2)
    cv2.imshow('Result', source_image)
    cv2.waitKey(0)
    return source_image
# def detect_template(template):
#         # Specify a threshold
#     threshold = 0.9
#     # take screenshot
#     im=ImageGrab.grab(bbox=(0,0, 1200, 800))
#     # im.show()
#     # template
#     wild = cv2.imread("images\\" + template + ".png", 0)

#     # convert to cv2 for matching
#     img_rgb = convert_from_image_to_cv2(im)

#     capR, capG, capB = cv2.split(img_rgb)
#     temR, temG, temB = cv2.split(cv2.imread("images\\" + template + ".png"))
#     resR = cv2.matchTemplate(capR, temR, cv2.TM_SQDIFF)
#     resG = cv2.matchTemplate(capG, temG, cv2.TM_SQDIFF)
#     resB = cv2.matchTemplate(capB, temB, cv2.TM_SQDIFF)
#     # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     # test = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
#     result = resR + resG + resB
#     # np.divide(result, 3)
#     # result = cv2.matchTemplate(img_rgb, wild, cv2.TM_SQDIFF_NORMED)
#     print(result)
#     loc = np.where(result >= threshold)
#     # dimensions of template
#     w, h = wild.shape[::-1]


#     # Store the coordinates of matched area in a numpy array
#     # loc = np.where(result >= threshold)
#     # Draw a rectangle around the matched region.
#     # flag for if wild was found
#     flag = False
#     for pt in zip(*loc[::-1]):
#         flag = True
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
#         # Show the final image with the matched area.

#     # if flag:
#     # print('wild pokemon appeared')
#     cv2.imshow('Template Detected', img_rgb)
#     cv2.waitKey(0)
#     return flag

    # TODO: check that the found wild is in the correct area
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, max_val, min_loc, max_loc)
    return False
detect_template('shiny_marill')

def saveClipboard(name):
    im = ImageGrab.grabclipboard()
    # im.show()
    im.save('images\\' + name + ".png")
# saveClipboard("bigmarill")
