def open_image(self):
    from PyQt5 import QtWidgets, QtCore
    from skimage import io
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        'Open File',
                                                        QtCore.QDir.rootPath(),
                                                        '*.*')
    try:
        self.source_image = io.imread(fileName)
        self.show_image(self.lblImage_1, self.source_image)
    except Exception as e:
        print('Error: {}'.format(e))