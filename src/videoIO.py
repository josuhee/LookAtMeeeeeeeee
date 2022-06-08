def show_video(label, image):
		import qimage2ndarray
		from PyQt5 import QtGui
		from PyQt5.QtCore import Qt

		image = qimage2ndarray.array2qimage(image)
		qpixmp = QtGui.QPixmap.fromImage(image)
		qpixmp = qpixmp.scaled(601, 291, aspectRatioMode=Qt.KeepAspectRatio)
		label.setPixmap(qpixmp)

class VideoIO:
	def __init__(self):
		self.source_image = None
		self.stop_webcam = False
		self.gray = False # Convert to grayscale
		self.rotate1 = False # Rotate 90
		self.rotate2 = False # Rotate 180
		self.rotate3 = False # Rotate 270

	def openVideo(self, label1, label2):
		import cv2
		import videoConvert as vc
		from PyQt5 import QtWidgets, QtCore

		self.stop_webcam = False
		self.gray = False
		self.rotate1 = False
		self.rotate2 = False
		self.rotate3 = False
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
														'Open File',
														QtCore.QDir.rootPath(),
														'*.*')
		cap = cv2.VideoCapture(fileName)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			show_video(label1, self.source_image)
			if self.gray:
				vc.graySacle(label2, self.source_image)
			if self.rotate1:
				vc.flip90(label2, self.source_image)
			if self.rotate2:
				vc.flip180(label2, self.source_image)
			if self.rotate3:
				vc.flip270(label2, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()

	def connectwebcam(self, label1, label2):
		import cv2
		import videoConvert as vc

		self.stop_webcam = False
		self.gray = False
		self.rotate1 = False
		self.rotate2 = False
		self.rotate3 = False

		cap = cv2.VideoCapture(0)
		while True:
			ret, self.source_image = cap.read()
			self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
			show_video(label1, self.source_image)
			if self.gray:
				vc.graySacle(label2, self.source_image)
			if self.rotate1:
				vc.flip90(label2, self.source_image)
			if self.rotate2:
				vc.flip180(label2, self.source_image)
			if self.rotate3:
				vc.flip270(label2, self.source_image)
			cv2.waitKey(24)
			if self.stop_webcam:
				break
		cap.release()
		cv2.destroyAllWindows()

	def stopwebcam(self):
		self.stop_webcam = True

	def convertGray(self):
		self.gray = True
		self.rotate1 = False
		self.rotate2 = False
		self.rotate3 = False

	def rotate90(self):
		self.rotate1 = True
		self.gray = False
		self.rotate2 = False
		self.rotate3 = False

	def rotate180(self):
		self.rotate2 = True
		self.gray = False
		self.rotate1 = False
		self.rotate3 = False

	def rotate270(self):
		self.rotate3 = True
		self.gray = False
		self.rotate1 = False
		self.rotate2 = False