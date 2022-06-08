class VideoIO:
	def __init__(self):
		self.source_image = None
		self.stop_webcam = False
		self.gray = False
		self.rotate1 = False
	
	def openVideo(self, label1, label2):
		import cv2
		import imageIO as iio
		import videoConvert as vc
		from PyQt5 import QtWidgets, QtCore

		self.stop_webcam = False
		self.gray = False
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
														'Open File',
														QtCore.QDir.rootPath(),
														'*.*')
		cap = cv2.VideoCapture(fileName)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			iio.show_image(label1, self.source_image)
			if self.gray:
				vc.graySacle(label2, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()

	def connectwebcam(self, label1, label2):
		import cv2
		import videoConvert as vc
		import imageIO as iio

		self.stop_webcam = False
		self.gray = False
		self.rotate1 = False

		cap = cv2.VideoCapture(0)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			iio.show_image(label1, self.source_image)
			if self.gray:
				vc.graySacle(label2, self.source_image)
			if self.rotate1:
				vc.flip90(label2, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()

	def stopwebcam(self):
		self.stop_webcam = True

	def convertGray(self):
		self.gray = True

	def rotate90(self):
		self.rotate1 = True
