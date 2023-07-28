import json
import math

import cv2
import numpy as np

from PIL import Image as Img
from PIL import ImageChops, ImageOps

from colour import Color
import webcolors


from collections import Counter
from PIL import Image as Img
from sklearn.cluster import KMeans

# import ruined
# from ruined import concretes_names, concretes, stones_names, stones, etces, etces_names

# concretes_names = ruined.concretes_names
# concretes = ruined.concretes
# stones_names = ruined.stones_names
# stones = ruined.stones
# etces = ruined.etces
# etces_names = ruined.etces_names
#
#
# all_block_names = concretes_names + etces_names + stones_names
# all_block_imgs = concretes + etces + stones


def get_dominant_color(image, k=4, image_processing_size=None):
    """
    takes an image as input
    returns the dominant color of the image as a list

    dominant color is found by running k means on the
    pixels & returning the centroid of the largest cluster

    processing time is sped up by working with a smaller image;
    this resizing can be done with the image_processing_size param
    which takes a tuple of image dims as input

    >>> get_dominant_color(image, k=4, image_processing_size = (25, 25))
    [56.2423442, 34.0834233, 70.1234123]
    """
    # resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size,
                           interpolation=cv2.INTER_AREA)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster and assign labels to the pixels
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image)

    # count labels to find most popular
    label_counts = Counter(labels)

    # subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

    return list(dominant_color)


def dom_rgb(pil_img: Img, clusters=None, img_size=None, as_list=None, return_comp=None):
    """
    returns tuple(r,g,b) of the dominant color as  of a PIL Img
    the image as a list using color_utils.dominant_color
    pil_img = Img.open('path/to/file.png')
    img_drgb(pil_img)
    [56.2423442, 34.0834233, 70.1234123]
    """
    if not clusters:
        clusters = 3
    if not img_size:
        img_size = (16, 16)

    # convert PIL Img to HSV np.array for opencv to call get_dominant_color
    bgr_image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    #
    dc = get_dominant_color(hsv_image, clusters, img_size)
    # create a square showing dominant color of equal size to input image
    dom_color_hsv = np.full(hsv_image.shape, dc, dtype='uint8')
    # convert to bgr color space for display
    dom_color_bgr = cv2.cvtColor(dom_color_hsv, cv2.COLOR_HSV2BGR)

    # retun_comp returns a side-by-side comparison img of the original texture vs the dominant color
    if return_comp:

        # combine the original image and the dominant color img
        output_image = np.hstack((bgr_image, dom_color_bgr))

        # convert back to RGB from BGR and return PIL Img
        out_im = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
        return Img.fromarray(out_im, mode="RGB")
    else:
        # convert dom color image to RGB and create a new Pil Img
        out_im = Img.fromarray(cv2.cvtColor(dom_color_bgr, cv2.COLOR_BGR2RGB))
        # load array of pixels
        px = out_im.load()
        # get the rgb of pixel 0,0
        ci_rgb = px[0, 0]
        return list(ci_rgb) if as_list else ci_rgb


def rgb_to_hex(rgb, with_hash=None):
    der_hex = '%02x%02x%02x' % rgb
    if with_hash:
        der_hex = f"#{der_hex}"
    return der_hex


def img_hex(pil_img, with_hash=None):
    rgbl = dom_rgb(pil_img)
    da_hex = rgb_to_hex(tuple(dom_rgb(pil_img)))
    if with_hash:
        da_hex = f"#{da_hex}"
    return da_hex


def img_compliment_rgb(pil_img, as_list=None):
    rgbl = dom_rgb(pil_img, as_list=True)
    compliment = [255 - rgbl[0], 255 - rgbl[1], 255 - rgbl[2]]
    return compliment if as_list else tuple(compliment)


def rgb_color_dist(rgb1: tuple, rgb2: tuple):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2

    diff = math.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)
    return diff


def normalize_lum(low, mid, high):
    #print("IN =>\t", low, "\t", mid, "\t", high)

    if mid > high:
        high = .9
    if mid < low:
        low = .05

    r_high = mid + ((high - mid) / 1.2)
    r_mid = mid
    r_low = (mid - low) / 2
    #print("out=>\t",r_low, "\t", r_mid, "\t", r_high, "\n")
    return ( r_low, r_mid, r_high)

def get_color_ramp(steps:int,
                   base_hex:str=None,
                   base_rgb:tuple=None,
                   light_lum=0.95,
                   dark_lum= 0.15):

    if base_rgb:
        r,g,b = base_rgb
        c = Color(rgb=(r/255, g/255, b/255))
    if base_hex and not base_rgb:
        c = Color(base_hex)
    if not base_hex and not base_rgb:
        return False

    low, mid, high = normalize_lum(dark_lum, c.get_luminance(), light_lum)
    # print(low, mid, high )
    light_tone = Color(hue=c.get_hue(), saturation=c.get_saturation(), luminance=high)
    dark_tone = Color(hue=c.get_hue(), saturation=c.get_saturation(), luminance=low)

    if base_rgb:
        ramp_list = [tone.get_rgb() for tone in dark_tone.range_to(light_tone, steps)]
        _ramp_list = [(int(_r * 255), int(_g * 255), int(_b * 255)) for (_r,_g,_b) in ramp_list]
        return tuple(_ramp_list)
    else:
        return tuple([color.get_web() for color in dark_tone.range_to(light_tone, 2)])


def colour_from_rgb_tuple(rgb_tuple:tuple):
    """ note spelling, this returns a colour.Color object"""
    r,g,b = rgb_tuple
    return Color(rgb=(r/255, g/255, b/255))


def colorize_overlay(pil_img, dark_rgb, light_rgb, mid_rgb=None):
    # we need to put the alpha channel aside
    _r, _g_, _b, im_alpha = pil_img.split()
    if mid_rgb:
        # image needs to be converted to grayscale for color ramp
        im_in_color = ImageOps.colorize(pil_img.convert('L'),
                                        dark_rgb, light_rgb, mid=mid_rgb)
    else:
        im_in_color = ImageOps.colorize(im_alpha.convert('L'), dark_rgb, light_rgb)
        # add alpha channel back to colorized image

    im_in_color.putalpha(im_alpha)
    return im_in_color


if __name__ == "__main__":
    print(' small demo of a few functions, print(ramp_list) or print(_ramp_list) to see')
    # print(rgb,get_color_ramp(base_rgb=c.get_rgb(), steps=2, light_lum=0.85, dark_lum=0.15))
    steps = 5
    rgb_tup =  (108, 80, 134)
    r,g,b = rgb_tup
    c = Color(rgb=(r/255, g/255, b/255))
    light_lum=0.85
    dark_lum= 0.2
    light_tone = Color(hue=c.get_hue(), saturation=c.get_saturation(), luminance=light_lum)
    dark_tone = Color(hue=c.get_hue(), saturation=c.get_saturation(), luminance=dark_lum)

    ramp_list = [tone.get_rgb() for tone in dark_tone.range_to(light_tone, steps)]

    _ramp_list = [(int(_r * 255), int(_g * 255), int(_b * 255)) for (_r,_g,_b) in
                  [tone.get_rgb() for tone in dark_tone.range_to(light_tone, steps)]]