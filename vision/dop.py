# Functions for the processing of DOP - Images
import numpy as np
import os, random


def get_from_folder(path, ending=".jpeg"):
    choice = random.choice(os.listdir(path))
    assert choice.endswith(ending), f"There are no .tif-Files at {path}"
    return choice


def get_rgb_img(tif_dop):
    """
    Returns a rgb image from a tif_dop (dataset format)
    :param tif_dop: The dop as loaded from rasterio
    :return rgb_img: The rgb image
    """

    tif_shp = tif_dop.read().shape
    assert tif_shp[0] == 3, f"Invalid tif shape: {tif_shp}"

    rgb_img = np.zeros((tif_shp[1], tif_shp[2], tif_shp[0]), 'uint8')
    rgb_img[..., 0] = tif_dop.read(1)
    rgb_img[..., 1] = tif_dop.read(2)
    rgb_img[..., 2] = tif_dop.read(3)

    return rgb_img

