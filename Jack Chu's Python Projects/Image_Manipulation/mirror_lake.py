"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    img = SimpleImage(filename)
    # the image we want to change
    new_img = SimpleImage.blank(img.width, img.height*2)
    # the new image should be two times height of the original image
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            new_pic_p1 = new_img.get_pixel(x, y)
            new_pic_p2 = new_img.get_pixel(x, new_img.height-1-y)
            new_pic_p1.red = img_p.red
            new_pic_p1.green = img_p.green
            new_pic_p1.blue = img_p.blue
            new_pic_p2.red = img_p.red
            new_pic_p2.green = img_p.green
            new_pic_p2.blue = img_p.blue
    return new_img


def main():
    """
    We need to change the pic we want to two times its height, with the original pic in it
    and the upside down of the pic under the original pic(just like the reflection).
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
