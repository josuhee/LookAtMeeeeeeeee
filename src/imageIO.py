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

def save_toJPEG(source_image):
    from PIL import Image
    from skimage import io
    io.imsave('../image/toJPEG.png', source_image)
    img = Image.open('../image/toJPEG.png').convert('RGB')
    img.save('../image/toJPEG.jpeg', 'jpeg')

def save_toPNG(source_image):
    from skimage import io
    io.imsave('../image/toPNG.png', source_image)

def save_toBMP(source_image):
    from PIL import Image
    from skimage import io
    io.imsave('../image/toBMP.png', source_image)
    img = Image.open('../image/toBMP.png').convert('RGB')
    img.save('../image/toBMP.bmp', 'bmp')