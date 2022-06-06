# Final
# 201812245 Chang Jiyoung
# 201812433 Jo Suhee

from PyQt5.QtWidgets import QMainWindow

class multimedia_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(multimedia_processing_class, self).__init__()
        loadUi('../ui/final_project_app.ui', self)
        self.source_image = None
        self.btnOpenimage.clicked.connect(lambda: self.open_image())

        self.btnShowhist.clicked.connect(lambda: self.show_histogram())

    def open_image(self):
        import imageIO as iio
        self.source_image = iio.open_image(self.source_image)
        self.show_image(self.lblImage_1, self.source_image)

    def show_image(self, label, image):
        import imageIO as iio
        iio.show_image(label, image)

    def show_histogram(self):
        import imageConvert01 as ic1
        from skimage import io
        ic1.show_histogram(self.source_image)
        hist_img = io.imread('hist.png')
        self.show_image(self.lblImage_2, hist_img)

def multi_processing_app():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = multimedia_processing_class()
    window.show()
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    multi_processing_app()