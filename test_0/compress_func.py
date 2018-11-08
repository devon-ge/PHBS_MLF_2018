from PIL import Image


def compress_image(img):
    """ compress a picture with `ratio' """
    com_img = Image.open(img)
    size = 256, 256
    com_img.thumbnail(size)
    com_img.save(f'com_{img}', 'png')
