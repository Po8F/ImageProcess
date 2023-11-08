import numpy as np


def RGB_avg_Grayscale(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            (B, G, R) = image[i, j]
            gray = (int(B) + int(G) + int(R)) / 3
            _return[i, j] = np.uint8(gray)
    return _return


def RGB_wei_Grayscale(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            (B, G, R) = image[i, j]
            gray = float(B) * 0.114 + float(G) * 0.587 + float(R) * 0.299
            _return[i, j] = np.uint8(gray)
    return _return


def Gray_pos_Binary(image, threshold):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            if image[i, j, 0] > threshold:
                _return[i, j] = np.uint8(255)
            else:
                _return[i, j] = np.uint8(0)
    return _return


def Gray_neg_Binary(image, threshold):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            if image[i, j, 0] < threshold:
                _return[i, j] = np.uint8(255)
            else:
                _return[i, j] = np.uint8(0)
    return _return


def EdgeDetection(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if image[i, j, 0] != image[i - 1, j, 0] or \
                    image[i, j, 0] != image[i, j - 1, 0] or \
                    image[i, j, 0] != image[i, j + 1, 0] or \
                    image[i, j, 0] != image[i + 1, j, 0]:
                _return[i, j] = np.uint8(255)
    return _return


def cut1(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(int(height)):
        for j in range(int(width / 4)):
            if int(image[i, j, 0]) == 255:
                _return[i, j] = 255
            else:
                _return[i, j] = 0
    return _return


def cut2(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(int(height)):
        for j in range(int(width / 4), int(width / 2)):
            if int(image[i, j, 0]) == 255:
                _return[i, j] = 255
            else:
                _return[i, j] = 0
    return _return


def cut3(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(int(height)):
        for j in range(int(width / 2), int(3 * width / 4)):
            if int(image[i, j, 0]) == 255:
                _return[i, j] = 255
            else:
                _return[i, j] = 0
    return _return


def cut4(image):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(int(height)):
        for j in range(int(3 * width / 4), width):
            if int(image[i, j, 0]) == 255:
                _return[i, j] = 255
            else:
                _return[i, j] = 0
    return _return


def cut(image, start, end):
    img_info = image.shape
    height = img_info[0]
    width = img_info[1]
    _return = np.zeros((height, width, 3), np.uint8)
    for i in range(int(height)):
        for j in range(int(width * start), int(width * end)):
            if int(image[i, j, 0]) == 255:
                _return[i, j] = 255
            else:
                _return[i, j] = 0
    return _return
