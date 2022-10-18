import numpy as np
import matplotlib.pyplot as plt
import scipy

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc
import scipy.misc
import matplotlib.pylab as pylab
import cv2
from matplotlib.colors import Normalize
import matplotlib.cm as cm

"""
image = cv2.imread("zelda.png")
(h, w, d) = image.shape
cv2.imshow("Image", image)
cv2.waitKey(0)
"""


def dct_function(b, fn3):
    img1 = cv2.imread(fn3, cv2.IMREAD_GRAYSCALE)
    h, w = np.array(img1.shape[:2])/b * b
    h = int(h)
    w = int(w)
    img1 = img1[:h, :w]

    blocksV = int(h/b)
    blocksH = int(w/b)
    vis0 = np.zeros((h, w), np.float32)
    Trans = np.zeros((h, w), np.float32)
    vis0[:h, :w] = img1

    for row in range(blocksV):
        for col in range(blocksH):
            currentblock = cv2.dct(vis0[row*b:(row+1)*b, col*b:(col+1)*b])
            Trans[row*b:(row+1)*b, col*b:(col+1)*b] = currentblock
    cv2.imwrite('Transformed.png', Trans)

    back0 = np.zeros((h, w), np.float32)
    for row in range(blocksH):
        for col in range(blocksH):
            currentblock = cv2.idct(Trans[row*b:(row+1)*b, col*b:(col+1)*b])
            back0[row*b:(row+1)*b, col*b:(col+1)*b] = currentblock
    cv2.imwrite('BackTransformed.png', back0)

    return back0
