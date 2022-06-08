from numpy import source


def graySacle(label, source_image):
	import cv2
	import imageIO as iio

	gray_image = cv2.cvtColor(source_image, cv2.COLOR_RGB2GRAY)
	iio.show_image(label, gray_image)

def flip90(label, source_image):
	import imageIO as iio
	import cv2

	im_rotated = cv2.rotate(source_image, cv2.ROTATE_90_CLOCKWISE)
	iio.show_image(label, im_rotated)

def flip180(label, source_image):
	import imageIO as iio
	import cv2

	im_rotated = cv2.rotate(source_image, cv2.ROTATE_180)
	iio.show_image(label, im_rotated)