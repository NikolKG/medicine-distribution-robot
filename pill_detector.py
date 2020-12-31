# USAGE
# python object_size.py --image images/example_01.png --width 0.955
# python object_size.py --image images/example_02.png --width 0.955
# python object_size.py --image images/example_03.png --width 3.5

# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


######################### take_pic_from_cam function #########################
# Function for take picture from camera
def take_pic_from_cam():
    cam = cv2.VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()
    return img


######################### save_pic_to_path function #########################
# Function for save picture in path
def save_pic_to_path(img, path):
    cv2.imwrite(path, img)


################## amount_of_pills function #######################
# Function for identifies the number of pills in cup using image recognition
def amount_of_pills():
    save_pic_to_path(take_pic_from_cam(), "/home/pi/PycharmProjects/HarelAz-Final-Project---drug-distribution-robot-/resuorses/temp.jpg")
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default="",
                    help="path to the input image")
    ap.add_argument("-w", "--width", type=float, default=0.5,
                    help="width of the left-most object in the image (in inches)")
    args = vars(ap.parse_args())

    # load the image, convert it to grayscale, and blur it slightly
    # image = cv2.imread(args["image"])
    image = cv2.imread("/home/pi/PycharmProjects/HarelAz-Final-Project---drug-distribution-robot-/resuorses/temp.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('gray', gray)
    #cv2.imshow('th', th)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 10, 100)
    #print(edged)
    #cv2.imshow('edged', edged)
    edged = cv2.dilate(th, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    #cv2.imshow('edged', edged)
    edged = th

    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts)

    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None

    orig = image.copy()
    orig2 = image.copy()
    # loop over the contours individually
    num_of_pill = 0
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 150 or cv2.contourArea(c) > 10000:
            continue
        num_of_pill+=1
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(orig2, ellipse, (255, 0, 255), 1, cv2.LINE_AA)

        # compute the rotated bounding box of the contour
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        # loop over the original points and draw them
        for (x, y) in box:
            cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

        # unpack the ordered bounding box, then compute the midpoint
        # between the top-left and top-right coordinates, followed by
        # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box
        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)

        # compute the midpoint between the top-left and top-right points,
        # followed by the midpoint between the top-righ and bottom-right
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

        # draw the midpoints on the image
        cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

        # draw lines between the midpoints
        cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                 (255, 0, 255), 2)
        cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                 (255, 0, 255), 2)

        # compute the Euclidean distance between the midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        # if the pixels per metric has not been initialized, then
        # compute it as the ratio of pixels to supplied metric
        # (in this case, inches)
        if pixelsPerMetric is None:
            pixelsPerMetric = dB / args["width"]

        # compute the size of the object
        dimA = dA / pixelsPerMetric
        dimB = dB / pixelsPerMetric

        # draw the object sizes on the image
        cv2.putText(orig, "{:.1f}in".format(dimA),
                    (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2)
        cv2.putText(orig, "{:.1f}in".format(dimB),
                    (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", orig)
    cv2.imshow("Image2", orig2)
    #print(num_of_pill)
    cv2.waitKey(0)
    return num_of_pill


if __name__ == "__main__":
    #save_pic_to_path(take_pic_from_cam(), "/home/pi/PycharmProjects/HarelAz-Final-Project---drug-distribution-robot-/resuorses/temp.jpg")
    amount_of_pills()
