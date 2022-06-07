def graySacle(label, source_image):
	import cv2
	import imageIO as iio

	gray_image = cv2.cvtColor(source_image, cv2.COLOR_RGB2GRAY)
	iio.show_image(label, gray_image)