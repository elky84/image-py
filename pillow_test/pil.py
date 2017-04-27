
from PIL import Image

#missing docstring
#http://pylint-messages.wikidot.com/messages:c0111

#invalid const naming
#const는 대문자랑, 숫자랑, _만 사용.
#http://pylint-messages.wikidot.com/messages:c0103

if __name__ == '__main__':
    print('PIL_Version : ' + Image.VERSION)
    print('PILLOW_Version : ' + Image.PILLOW_VERSION)

    PYTHON_IMAGE = Image.open("python.jpg")
    print('SOURCE IMAGE {} FORMAT {}'.format(PYTHON_IMAGE.size, PYTHON_IMAGE.format))

    PYTHON_RESIZE_IMAGE = PYTHON_IMAGE.resize((100, 100), Image.ANTIALIAS)

    print('RESIZE IMAGE {} FORMAT {}'.format(PYTHON_RESIZE_IMAGE.size, PYTHON_RESIZE_IMAGE.format))

    PYTHON_RESIZE_IMAGE.save("python_resize.jpg", "JPEG")

    PYTHON_RESIZE_CROP = PYTHON_IMAGE.crop((0, 0, 100, 100))
    print('CROP IMAGE {} FORMAT {}'.format(PYTHON_RESIZE_CROP.size, PYTHON_RESIZE_CROP.format))

    PYTHON_RESIZE_CROP.save("python_crop.jpg", "JPEG")

    #PYTHON_IMAGE.show()
