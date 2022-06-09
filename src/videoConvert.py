def graySacle(label, source_image):
	import videoIO as vio
	import cv2

	gray_image = cv2.cvtColor(source_image, cv2.COLOR_RGB2GRAY)
	vio.show_video(label, gray_image)

def flip90(label, source_image):
	import videoIO as vio
	import cv2

	im_rotated = cv2.rotate(source_image, cv2.ROTATE_90_CLOCKWISE)
	vio.show_video(label, im_rotated)

def flip180(label, source_image):
	import videoIO as vio
	import cv2

	im_rotated = cv2.rotate(source_image, cv2.ROTATE_180)
	vio.show_video(label, im_rotated)

def flip270(label, source_image):
	import videoIO as vio
	import cv2

	im_rotated = cv2.rotate(source_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
	vio.show_video(label, im_rotated)

def detectBicycle(label, source_image, model):
	import videoIO as vio

	results = model(source_image)
	detect_image = results.show()
	vio.show_video(label, detect_image)