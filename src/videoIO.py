class VideoIO:
	def __init__(self):
		self.source_image = None
		self.stop_webcam = False
	
	def openVideo(self, label):
		import cv2
		import imageIO as iio
		from PyQt5 import QtWidgets, QtCore

		self.stop_webcam = False
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
														'Open File',
														QtCore.QDir.rootPath(),
														'*.*')
		cap = cv2.VideoCapture(fileName)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			iio.show_image(label, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()

	def connectwebcam(self, label):
		import cv2
		import imageIO as iio

		self.stop_webcam = False

		cap = cv2.VideoCapture(0)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			iio.show_image(label, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()
