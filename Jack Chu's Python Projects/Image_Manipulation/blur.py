"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = img
    # make change on the new image
    for x in range(img.width):
        for y in range(img.height):
            old_p = img.get_pixel(x, y)
            new_p = new_img.get_pixel(x, y)
            # it's the pixel in the middle of its other 8 neighbors
            if x+y == 0:
                # if on the left up corner
                old_p6 = img.get_pixel(x + 1, y)
                old_p8 = img.get_pixel(x, y + 1)
                old_p9 = img.get_pixel(x + 1, y + 1)
                avr_red = (old_p6.red+old_p8.red+old_p9.red)//3
                avr_blue = (old_p6.blue+old_p8.blue+old_p9.blue)//3
                avr_green = (old_p6.green+old_p8.green+old_p9.green)//3
            elif x == img.width-1 and y == 0:
                # if on the right up corner
                old_p4 = img.get_pixel(x - 1, y)
                old_p7 = img.get_pixel(x - 1, y + 1)
                old_p8 = img.get_pixel(x, y + 1)
                avr_red = (old_p4.red + old_p7.red + old_p8.red) // 3
                avr_blue = (old_p4.blue + old_p7.blue + old_p8.blue) // 3
                avr_green = (old_p4.green + old_p7.green + old_p8.green) // 3
            elif x == 0 and y == img.height-1:
                # if on the left down corner
                old_p2 = img.get_pixel(x, y - 1)
                old_p3 = img.get_pixel(x + 1, y - 1)
                old_p6 = img.get_pixel(x + 1, y)
                avr_red = (old_p2.red + old_p3.red + old_p6.red) // 3
                avr_blue = (old_p2.blue + old_p3.blue + old_p6.blue) // 3
                avr_green = (old_p2.green + old_p3.green + old_p6.green) // 3
            elif x == img.width-1 and y == img.height-1:
                # if on the right down corner
                old_p1 = img.get_pixel(x - 1, y - 1)
                old_p2 = img.get_pixel(x, y - 1)
                old_p4 = img.get_pixel(x - 1, y)
                avr_red = (old_p1.red + old_p2.red + old_p4.red) // 3
                avr_blue = (old_p1.blue + old_p2.blue + old_p4.blue) // 3
                avr_green = (old_p1.green + old_p2.green + old_p4.green) // 3
            elif x == 0 and y != 0 and y != img.height-1:
                # if on the lft side
                old_p2 = img.get_pixel(x, y - 1)
                old_p3 = img.get_pixel(x + 1, y - 1)
                old_p6 = img.get_pixel(x + 1, y)
                old_p8 = img.get_pixel(x, y + 1)
                old_p9 = img.get_pixel(x + 1, y + 1)
                avr_red = (old_p2.red + old_p3.red + old_p6.red + old_p8.red + old_p9.red) // 5
                avr_blue = (old_p2.blue + old_p3.blue + old_p6.blue + old_p8.blue + old_p9.blue) // 5
                avr_green = (old_p2.green + old_p3.green + old_p6.green + old_p8.green + old_p9.green) // 5
            elif y == 0 and x != 0 and x != img.width-1:
                # if on the upper side
                old_p4 = img.get_pixel(x - 1, y)
                old_p6 = img.get_pixel(x + 1, y)
                old_p7 = img.get_pixel(x - 1, y + 1)
                old_p8 = img.get_pixel(x, y + 1)
                old_p9 = img.get_pixel(x + 1, y + 1)
                avr_red = (old_p4.red + old_p6.red + old_p7.red + old_p8.red + old_p9.red) // 5
                avr_blue = (old_p4.blue + old_p6.blue + old_p7.blue + old_p8.blue + old_p9.blue) // 5
                avr_green = (old_p4.green + old_p6.green + old_p7.green + old_p8.green + old_p9.green) // 5
            elif x == img.width-1 and y != 0 and y != img.height-1:
                # if on the right side
                old_p1 = img.get_pixel(x - 1, y - 1)
                old_p2 = img.get_pixel(x, y - 1)
                old_p4 = img.get_pixel(x - 1, y)
                old_p7 = img.get_pixel(x - 1, y + 1)
                old_p8 = img.get_pixel(x, y + 1)
                avr_red = (old_p1.red + old_p2.red + old_p4.red + old_p7.red + old_p8.red) // 5
                avr_blue = (old_p1.blue + old_p2.blue + old_p4.blue + old_p7.blue + old_p8.blue) // 5
                avr_green = (old_p1.green + old_p2.green + old_p4.green + old_p7.green + old_p8.green) // 5
            elif y == img.height-1 and x != 0 and x != img.width-1:
                # if on the down side
                old_p1 = img.get_pixel(x - 1, y - 1)
                old_p2 = img.get_pixel(x, y - 1)
                old_p3 = img.get_pixel(x + 1, y - 1)
                old_p4 = img.get_pixel(x - 1, y)
                old_p6 = img.get_pixel(x + 1, y)
                avr_red = (old_p1.red + old_p2.red + old_p3.red + old_p4.red + old_p6.red) // 5
                avr_blue = (old_p1.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p6.blue) // 5
                avr_green = (old_p1.green + old_p2.green + old_p3.green + old_p4.green + old_p6.green) // 5
            else:
                old_p1 = img.get_pixel(x - 1, y - 1)
                old_p2 = img.get_pixel(x, y - 1)
                old_p3 = img.get_pixel(x + 1, y - 1)
                old_p4 = img.get_pixel(x - 1, y)
                old_p6 = img.get_pixel(x + 1, y)
                old_p7 = img.get_pixel(x - 1, y + 1)
                old_p8 = img.get_pixel(x, y + 1)
                old_p9 = img.get_pixel(x + 1, y + 1)
                avr_red = (old_p1.red+old_p2.red+old_p3.red+old_p4.red+old_p6.red+old_p7.red+old_p8.red+old_p9.red) // 8
                avr_blue = (old_p1.blue+old_p2.blue+old_p3.blue+old_p4.blue+old_p6.blue+old_p7.blue+old_p8.blue+old_p9.blue) // 8
                avr_green = (old_p1.green+old_p2.green+old_p3.green+old_p4.green+old_p6.green+old_p7.green+old_p8.red+old_p9.green)//8
            new_p.red = avr_red
            new_p.green = avr_green
            new_p.blue = avr_blue
    return new_img


def main():
    """
    We need to blur the image we want and also we can decide the degree of the blur,
    we will use the average color of a pixel's neighbors to decide the new pixel's color
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(8):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
