import numpy as np
import cv2


def split_img(img):
    '''

    :param img:
    :return:     12
                34
    '''
    row, col = img.shape
    left_top_img = img[:row // 2, :col // 2]
    right_top_img = img[:row // 2, col // 2:]
    left_down_img = img[row // 2:, :col // 2]
    right_down_img = img[row // 2:, col // 2:]

    return [left_top_img, right_top_img, left_down_img, right_down_img], [[0, 0], [0, col // 2], [row // 2, 0],
                                                                          [row // 2, col // 2]]


def green_point_dec(img,offset):
    center = [offset[0],offset[1]]
    return center
