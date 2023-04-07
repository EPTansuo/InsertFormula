#/usr/bin/python

from PIL import Image,ImageOps


def proc(filename):
    image = Image.open(filename+".png")
    image = image.convert("L")
    ivt_image = ImageOps.invert(image)
    bbox = ivt_image.getbbox()
    cropped_image = image.crop(bbox)
    cropped_image.save(filename+".jpg") 
