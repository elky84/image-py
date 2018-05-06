#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import glob
from shutil import copy


def dhash(image, hash_size=8):
    # Grayscale and shrink the image in one step.
    image = image.convert('L').resize(
        (hash_size + 1, hash_size),
        Image.ANTIALIAS,
    )

    pixels = list(image.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)


def img_diff(orig, modif, hash_size):
    # hash_size로 이미지의 정확도를 조절합니다.
    # 높을수록 비교 정확도가 올라가고 낮을수록 비교 정확도가 내려갑니다.

    # crop은 이미지를 자르는 명령이다.
    # 이미지를 자른 이유는 빨간색 LED가 계속 깜빡거리며 나오기 때문에 그 부분을 제외시키려고 잘랐다.
    # 이미지를 비교할때만 자르는 것이고 원본은 그대로 있다.
    o = Image.open(orig).crop((0, 0, 1920, 800))
    m = Image.open(modif).crop((0, 0, 1920, 800))
    if dhash(o, hash_size) != dhash(m, hash_size):
        print("Difference Image {0} / {1}".format(orig, modif))
        # 첫번째 이미지와 두번째 이미지가 다르다면 첫번째 이미지를 event디렉토리로 복사합니다.
        copy(orig, "event/") # event 디렉토리는 이미 만들어져 있어야 합니다.


# 이미지 파일이 위치한 곳에서 스크립트를 실행해야 합니다.
if __name__ == '__main__':
    file_list = glob.glob('*')

    for idx, f in enumerate(file_list):
        try:
            img_diff(f, file_list[idx+1], 4)
        except IndexError as e:
            print(e)