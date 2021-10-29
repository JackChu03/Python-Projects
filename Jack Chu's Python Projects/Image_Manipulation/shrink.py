"""
Name: Jack Chu
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)
    # to make half the size of the original picture
    for x in range(shrink_img.width):
        for y in range(shrink_img.height):
            shrink_p = shrink_img.get_pixel(x, y)
            img_p = img.get_pixel(x * 2, y * 2)
            # to decide what pixel to get from the original picture
            shrink_p.red = img_p.red
            shrink_p.green = img_p.green
            shrink_p.blue = img_p.blue
    return shrink_img


def main():
    """
    We need to shrink the original picture to half with the content of the picture unchanged
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
