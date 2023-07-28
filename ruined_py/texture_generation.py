import blend_modes
import numpy as np
from PIL import Image as Img
from PIL import ImageChops, ImageOps


def get_rgba(path):
    _img = Img.open(path)
    _img = _img.convert('RGBA')
    return _img


def get_mask(rgba_img):
    r, _g, _b, _alpha = rgba_img.split()
    _mask = ImageOps.invert(_alpha)
    return _mask


# texturizing PIL Imgs

specks_1 = Img.open('res16/specks_multiply_18_38_alpha.png')
specks_2 = Img.open('res16/specks_multiply_29_alpha.png')
contrasty_noise = Img.open('res16/specks_darken_10_45.png')
mellow_noise = Img.open('res16/saturation_52.png')

# mosses

moss_trans1 = Img.open('res16/mossy_0.png')
moss_trans2 = Img.open('res16/mossy_0b.png')
moss_a = Img.open('res16/mossy_a.png')
moss_b = Img.open('res16/mossy_b.png')
moss_c = Img.open('res16/mossy_c.png')

# photoshop-esque layer-ish blending

# dodge and burn
dodge = blend_modes.dodge
soft_light = blend_modes.soft_light
hard_light = blend_modes.hard_light
lighten_only = blend_modes.lighten_only
darken_only = blend_modes.darken_only

multiply = blend_modes.multiply

grain_extract = blend_modes.grain_extract
grain_merge = blend_modes.grain_merge
# more specialized
difference = blend_modes.difference
addition = blend_modes.addition
subtract = blend_modes.subtract
divide = blend_modes.divide


def img_blend(pil_bg, pil_fg, func, opacity=.33):
    """
        pass two PIL Images, a blendmode function passed as func ,
        and a float opacity value (between .01 and .99 I guess?)
        (e.g.
            background_img = Image.open(path_to_bg_file)
            foreground_img = Image.open(path_to_fg_file)
            img_blend(background_img, foreground_img, blend_modes.multiply, .25)
        )
    :param pil_bg: PIL.Image.Image
    :param pil_fg: PIL.Image.Image
    :param func: function (from blendmodes)
    :param opacity:
    :return:
    """
    # Import background image
    background_img_raw = pil_bg.convert('RGBA')  # RGBA image
    background_img = np.array(background_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    # Import foreground image
    foreground_img_raw = pil_fg.convert('RGBA')  # RGBA image
    foreground_img = np.array(foreground_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.
    # Blend images
    # opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
    blended_img_float = func(background_img_float, foreground_img_float, opacity)

    # Convert blended image back into PIL image-compatible uint8 array
    blended_img = np.uint8(blended_img_float)
    # Image needs to be converted back to uint8 type for PIL handling.

    # return a PIL Image
    return Img.fromarray(blended_img)


# brick generation

big_brick_grout = Img.open('res16/big_bricks_grout.png')
big_brick_grout_lighter = Img.open('res16/big_bricks_lighter_grout.png')
big_brick_burn = Img.open('res16/big_bricks_shadow.png')
big_brick_dodge = Img.open('res16/big_bricks_highlight.png')
big_brick_3d = Img.open('res16/big_bricks_highlight_shadow.png')


def big_brick(pil_img: Img, brick_pattern, db_amt=.07, ba=.08, ha=.1, extra=False, blend_step=False, blend_amt=1.0):
    _img = pil_img.convert('RGBA')
    _r, _g, _b, _burn_alpha = big_brick_burn.split()
    _r, _g, _b, _dodge_alpha = big_brick_dodge.split()
    _r, _g, _b, _alpha = brick_pattern.split()

    bb_burn_mask = get_mask(big_brick_burn)
    bb_dodge_mask = get_mask(big_brick_dodge)
    bb_grout_mask = get_mask(brick_pattern)

    # highlight big_brick_dodge /shadow big_brick_burn / both big_brick_3d

    # _img = pil_img + brick__pattern masked to the grout pattern alpha channel
    _img = ImageChops.composite(_img, brick_pattern, bb_grout_mask)

    # _img =
    _burn = ImageChops.blend(_img, big_brick_burn, ba)
    _img = ImageChops.composite(_img, _burn, bb_burn_mask)

    _dodge = ImageChops.blend(_img, big_brick_dodge, ha)
    _img = ImageChops.composite(_img, _burn, bb_dodge_mask)

    if extra:
        deep_brick = ImageChops.blend(_img, big_brick_3d, .18)
        # _img = ImageChops.blend(_img, big_brick_3d, db_amt)
        # burn

        bb_copy_100 = Img.open('res16/big_bricks_grout_copy_mask.png')
        _finish_mask = get_mask(bb_copy_100)
        # dodge
        _img = ImageChops.composite(_img, deep_brick, _finish_mask)

    if blend_step:
        _img_blend = ImageChops.blend(pil_img.convert('RGBA'), _img, blend_amt)
        return _img_blend
    return _img


sm_brick_grout = Img.open('res16/bricks_darker_grout.png')
sm_brick_grout_lighter = Img.open('res16/bricks_darker_grout.png')

sm_brick_burn = Img.open('res16/sm_bricks_shadow.png')
sm_brick_dodge = Img.open('res16/sm_bricks_highlight.png')
sm_brick_3d = Img.open('res16/sm_bricks_highlight_shadow.png')


def small_brick(pil_img: Img, brick_pattern, db_amt=.07, ba=.08, ha=.1, extra=True, blend_step=False, blend_amt=1.0):
    _img = pil_img.convert('RGBA')
    _r, _g, _b, _burn_alpha = sm_brick_burn.split()
    _r, _g, _b, _dodge_alpha = sm_brick_dodge.split()
    _r, _g, _b, _alpha = brick_pattern.split()

    sb_burn_mask = get_mask(sm_brick_burn)
    sb_dodge_mask = get_mask(big_brick_dodge)
    sb_grout_mask = get_mask(brick_pattern)

    # highlight big_brick_dodge /shadow big_brick_burn / both big_brick_3d

    # _img = pil_img + brick__pattern masked to the grout pattern alpha channel
    _img = ImageChops.composite(_img, brick_pattern, sb_grout_mask)

    # _img =
    _burn = ImageChops.blend(_img, big_brick_burn, ba)
    _img = ImageChops.composite(_img, _burn, sb_burn_mask)

    _dodge = ImageChops.blend(_img, big_brick_dodge, ha)
    _img = ImageChops.composite(_img, _burn, sb_dodge_mask)

    if extra:
        deep_brick = ImageChops.blend(_img, sm_brick_3d, .18)
        # _img = ImageChops.blend(_img, big_brick_3d, db_amt)
        # burn

        bb_copy_100 = Img.open('res16/sm_bricks_grout_copy_mask.png')
        _finish_mask = get_mask(bb_copy_100)
        # dodge
        _img = ImageChops.composite(_img, deep_brick, _finish_mask)

    if blend_step:
        _img_blend = ImageChops.blend(pil_img.convert('RGBA'), _img, blend_amt)
        return _img_blend
    return _img


def composite(pil_img_bg: Img, pil_img_fg: Img, size: tuple = (0, 0)):
    # im_out = pil_img_bg.copy()
    # im_out.paste(pil_img_fg, size, pil_img_fg)
    im_out = Img.alpha_composite(pil_img_bg, pil_img_fg)
    return im_out.convert('RGBA')
