import cv2


class ImageProcessing:

    def __init__(self):
        self._regular_image = None
        self._gray_image = None
        self._edged_image = None
        self._thresh_image = None

    def reset_object(self):
        self._regular_image = None
        self._gray_image = None
        self._edged_image = None
        self._thresh_image = None

    def load_image(self, path):
        self._regular_image = cv2.imread(path)

    @staticmethod
    def display_image(image, windows_name=None):
        cv2.imshow("windows" if not windows_name else windows_name, image)
        cv2.waitKey(0)

    def gray_image(self):
        self._gray_image = cv2.cvtColor(self._regular_image, cv2.COLOR_BGR2GRAY)

    def edged_image(self):
        self._gray_image = cv2.Canny(self._gray_image, 30, 150)

    def thresh_image(self):
        self._thresh_image = cv2.threshold(self._gray_image, 255, 255, cv2.THRESH_BINARY_INV)[1]
