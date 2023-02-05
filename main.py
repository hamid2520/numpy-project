# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import random
import time


def print_hi(name):

    img = cv2.imread("images.jpg", 0)

    m, n = 2, 2
    h, w = img.shape
    block_h, block_w = h // m, w // n
    blocks = [img[i:i + block_h, j:j + block_w] for i in range(0, h, block_h) for j in range(0, w, block_w)]

    for i, block in enumerate(blocks):
        result = np.zeros_like(img)
        if i == 0:
            block = cv2.addWeighted(block, 1, np.zeros_like(block), 0, 0)
        else:
            block = cv2.addWeighted(block, 1 + (i - 1) * 0.1, np.zeros_like(block), 0, 0)
        result[(i // n) * block_h:(i // n + 1) * block_h, (i % n) * block_w:(i % n + 1) * block_w] = block
        cv2.imshow("Result", result)
        cv2.waitKey(1000)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
