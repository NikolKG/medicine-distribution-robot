import cv2
import numpy as np

from ImageProcessing import ImageProcessing


def is_images_equal(sample_image1_path, sample_image2_path):
    """
    comparing two images and retrieve if the images are the same.
    :param sample_image1_path: path to sample image1
    :param sample_image2_path: path to sample image2
    :return: False/True
    """
    original = cv2.imread(sample_image1_path)
    duplicate = cv2.imread(sample_image2_path)

    shape_flag = True
    sub_flag = True

    if original.shape != duplicate.shape:  # check if the images size not match
        # print("The images have same size and channels")
        shape_flag = False

    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)
    if not (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
        sub_flag = False

    return shape_flag and sub_flag


def take_pic_from_cam():
    cam = cv2.VideoCapture(1)  # 0 -> index of camera
    s, img = cam.read()

    return img


def save_pic_to_path(img, path):
    cv2.imwrite(path, img)


def detect_object():
    pass


if __name__ == "__main__":
    pass
    # result1 = is_images_equal("resuorses/bob-sponge-sample1.jpg", "resuorses/bob-sponge-sample2.jpg")
    # print("result1 image_compare: ", result1)
    #
    # result2 = is_images_equal("resuorses/bob-sponge-sample1.jpg", "resuorses/bob-sponge-sample1.jpg")
    # print("result2 image_compare: ", result2)
    #
    #
    # save_pic_to_path(take_pic_from_cam(), "resuorses/test1.jpg")
    # time.sleep(5)
    # save_pic_to_path(take_pic_from_cam(), "resuorses/test2.jpg")
    # result3 = is_images_equal("resuorses/test1.jpg", "resuorses/test2.jpg")
    # print("result3 image_compare: ", result3)
    # print("result3 image_compare: ", result3)

    # save_pic_to_path(take_pic_from_cam(), "resuorses/test7.jpg")

    image_list = ["test7.jpg","test10.jpg", "test11.jpg", "test12.jpg", "test13.jpg", "test14.jpg", "test15.jpg", "test16.jpg",
                  "test17.jpg"]

    obj = ImageProcessing()
    obj.load_image("resuorses/" + image_list[0])
    obj.gray_image()

    circles = cv2.HoughCircles(obj._gray_image, cv2.HOUGH_GRADIENT, dp=1.5, minDist=50, param1=20, param2=0.9,
                               minRadius=0,
                               maxRadius=30)
    print("num of circle: ", len(circles[0]))

    output = obj._regular_image.copy()
    diameter = []
    materials = []
    coordinates = []

    count = 0
    if circles is not None:
        # append radius to list of diameters (we don't bother to multiply by 2)
        for (x, y, r) in circles[0, :]:
            diameter.append(r)

        # convert coordinates and radii to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over coordinates and radii of the circles
        for (x, y, d) in circles:
            count += 1

            # add coordinates to list
            coordinates.append((x, y))

            # extract region of interest
            space = 10
            roi = obj._regular_image[y - d - space:y + d + space, x - d - space:x + d + space]
            # draw contour and results in the output image
            cv2.circle(output, (x, y), d, (0, 255, 0), 2)

    ImageProcessing.display_image(output)
    #ImageProcessing.display_image(obj._regular_image)
    #ImageProcessing.display_image(obj._gray_image)
