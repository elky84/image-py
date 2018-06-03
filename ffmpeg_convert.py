#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

files = os.listdir(os.getcwd())

if __name__ == '__main__':
	for i in files:
		if i.endswith('.mp4'):
			os.system("ffmpeg -i {} -r 16 -t 30 {}-%2d.jpeg".format(i, i))