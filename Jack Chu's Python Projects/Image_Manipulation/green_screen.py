"""
Name: Jack Chu
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_p = figure_img.get_pixel(x, y)
            # to get each pixel in the figure picture
            background_p = background_img.get_pixel(x, y)
            # to get each pixel in the background picture
            bigger = max(figure_p.red, figure_p.blue)
            if figure_p.green > bigger * 2:
                # determine if the background of the figure picture is green screen
                figure_p.red = background_p.red
                figure_p.blue = background_p.blue
                figure_p.green = background_p.green
    return figure_img
    # the original figure picture is permanently finished changing to the one without green screen


def main():
    """
    We need to combine two pictures, the first one is a figure in the green screen and the second
    one is the background picture, and change the green screen in the figure picture to the background
    of the background picture.

    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
