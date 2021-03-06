"""
stanCodoshop Project
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

Name: Jack Chu

Description: To Remove the seemly human figure on the pictures we sent in, make these codes to learn
             from the pictures and return a picture that is without a human figure~
-----------------------------------------------
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    # the calculus of pixel distance to the average pixel
    color_dist = math.sqrt(((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2))
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively
    """
    t_red = 0
    t_blue = 0
    t_green = 0
    for points in pixels:
        t_red = t_red + points.red
        t_blue = t_blue + points.blue
        t_green = t_green + points.green
    avg_r = t_red // len(pixels)
    avg_b = t_blue // len(pixels)
    avg_g = t_green // len(pixels)
    return avg_r, avg_g, avg_b


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    # randomly choose the smallest distance between average and the pixel, and the best pixel
    smallest_dis = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])
    best_pixel = pixels[0]
    for points in pixels:
        dis = get_pixel_dist(points, avg[0], avg[1], avg[2])
        if dis < smallest_dis:
            # if somewhat a pixel's distance to average pixel's distance is shorter, the pixel replaces the best pixel
            best_pixel = points
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    pixels = []
    for x in range(width):
        for y in range(height):
            for img in images:
                # to get each image's same location pixel and compete them to get the best one
                pixel = img.get_pixel(x, y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)
            pixels = []
            # once get the best pixel, fit it in the new blank picture
            r_pixel = result.get_pixel(x, y)
            r_pixel.red = best_pixel.red
            r_pixel.green = best_pixel.green
            r_pixel.blue = best_pixel.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
