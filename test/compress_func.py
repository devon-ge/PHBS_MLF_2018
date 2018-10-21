from PIL import Image


def compress_image(img, ratio=0.5):
    """ compress a picture with `ratio' """
    com_img = Image.open(img)
    size = com_img.size[0]*ratio, com_img.size[1]*ratio
    com_img.thumbnail(size)
    com_img.save(f'{ratio}_{img}', 'png')

compress_image('test.png')