def open_image(source_image):
    from PyQt5 import QtWidgets, QtCore
    from skimage import io
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                        'Open File',
                                                        QtCore.QDir.rootPath(),
                                                        '*.*')
    try:
        source_image = io.imread(fileName)
        return source_image
    except Exception as e:
        print('Error: {}'.format(e))

def show_image(label, image):
    import qimage2ndarray
    from PyQt5 import QtGui
    
    image = qimage2ndarray.array2qimage(image)
    qpixmp = QtGui.QPixmap.fromImage(image)
    label.setPixmap(qpixmp)