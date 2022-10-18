# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from rgb_yuv import rgb_to_yuv
from rgb_yuv import yuv_tu_rgb
from run_lenght import run_lenght
from run_lenght import run_lenght_letters
from dct import dct_function

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Exercise 1: We call function with already given numbers (they can by changed, of course) and they return the YUV
    # values.
    r = 100
    g = 100
    b = 100

    y, u, v = rgb_to_yuv(r, g, b)
    print('\n')
    print('Exercise 1:')
    print('Els valors YUV corresponents als valors RGB de R = ', r, ', G = ', g, 'i B = ', b, 'son: Y = ', y, ', U = ',
          u, 'i V = ', v,'.')

    # We do the same with the RGB values.
    r1, g1, b1 = yuv_tu_rgb(y, u, v)
    print('Els valors RGB corresponents als valors YUV de Y = ', y, ', U = ', u, 'i V = ', v, 'son: R = ', r, ', G = ',
          g, 'i B = ', b, '.\n')

    # Exercise 4: As it wasn't explicitly explained, I've done two different functions, one that applies run-length
    # encoding to integer numbers, and another to a letters array.
    l = [1, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 10, 0, 0]
    list1 = run_lenght(l)
    print('Exercise 4:')
    print('El resultat del "run-length encoding" en el llistat numèric introduït és: ', list1)

    llista = 'aabbbdddsbaaj'
    a = run_lenght_letters(llista)
    print('El resultat del "run-length encoding" en el llistat de lletres introduït és: ', a, '\n')

    # Exercise 5: DCT function where you select the box size of the DCT function and the image that you want to apply
    # it.
    b = 8
    foto = dct_function(b, 'zelda.png')
    print('Exercise 5 :')
    print('Al executar la funció, es creen dues imatges amb el nom de Transformed.jpg i BackTransformed.jpg, les quals '
          'son el resultat d''aplicar \nel DCT a la imatge inicial, en aquest cas, zelda.png.')
    # The Transformed value and the result in the image are written and created once you execute the function. Check the
    # result images on the project file.
