"""
Name: Jack Chu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:
    :return:
    """
    high_light_p = SimpleImage(filename)
    for pixel in high_light_p:
        avr = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red > avr * HURDLE_FACTOR:
            # if we detect the file(which is color orange and yellow in the original pic)
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avr
            pixel.blue = avr
            pixel.green = avr
    return high_light_p
    # we completely change the original pic to the highlighted one


def main():
    """
    We need to detect the fire in the pic we want, and thus change the pic to
    the one only and clearly highlights the file(color red)
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
