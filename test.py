import cv2
import numpy as np
from PIL import ImageGrab, Image
from detect import convert_from_image_to_cv2



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


def color_template_matching(template_image):
    grab = ImageGrab.grab(bbox=(0,0, 1200, 800))
    source_image = convert_from_image_to_cv2(grab)
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

    return source_image

# Load the source and template images
# source_image = cv2.imread('images\\bigmarill.png')
template_image = cv2.imread('images\\smarill.png')

# Perform color-based template matching
result_image = color_template_matching(template_image)

# Display the result
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
