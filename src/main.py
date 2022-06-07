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
        self.btnInvert.clicked.connect(lambda: self.invert_image())

        self.btnHistEqual.clicked.connect(lambda: self.enhance_by_histequal())
        self.btnGamma.clicked.connect(lambda: self.enhance_by_gammacorrect())

        self.btnBlur.clicked.connect(lambda: self.blur_image())
        self.btnSmooth.clicked.connect(lambda: self.smooth_image())
        self.btnSharp.clicked.connect(lambda: self.sharp_image())

        self.btnRotate.clicked.connect(lambda: self.rotate_image())
        self.btnScaling.clicked.connect(lambda: self.scaling_image())
        self.btnFlipimage_left.clicked.connect(lambda: self.flip_image_left())
        self.btnFlipimage_top.clicked.connect(lambda: self.flip_image_top())
        self.btnWarpimage_row.clicked.connect(lambda: self.warp_image_row())
        self.btnWarpimage_col.clicked.connect(lambda: self.warp_image_col())

    def open_image(self):
        import imageIO as iio
        self.source_image = iio.open_image(self.source_image)
        self.show_image(self.lblImage_1, self.source_image)

    def show_image(self, label, image):
        import imageIO as iio
        iio.show_image(label, image)

    def show_histogram(self):
        import imageConvert01 as ic1
        from skimage import imread
        ic1.show_histogram(self.source_image)
        hist_img = imread('hist.png')
        self.show_image(self.lblImage_2, hist_img)

    def invert_image(self):
        import imageConvert01 as ic1
        from skimage.io import imread
        a_max = float(self.txtAmax.toPlainText())
        ic1.invert_image(self.source_image, a_max)
        invert_img = imread('invert.png')
        self.show_image(self.lblImage_2, invert_img)

    def enhance_by_histequal(self):
        import imageEnhance as ie
        from skimage.io import imread
        ie.enhance_by_histequal(self.source_image)
        histequal_img = imread('../image/enhance_hist_equal.png')
        self.show_image(self.lblImage_2, histequal_img)

    def enhance_by_gammacorrect(self):
        import imageEnhance as ie
        from skimage.io import imread
        ie.enhance_by_gammacorrect(self.source_image)
        gammacorrect_img = imread('../image/enhance_gamma_correct.png')
        self.show_image(self.lblImage_2, gammacorrect_img)

    def blur_image(self):
        import imageFilter as ifil
        from skimage.io import imread
        sigma = int(self.txtBlur.toPlainText())
        ifil.blur_image(self.source_image, sigma)
        blur_img = imread('../image/blurImage.png')
        self.show_image(self.lblImage_2, blur_img)

    def smooth_image(self):
        import imageFilter as ifil
        from skimage.io import imread
        ifil.smooth_image(self.source_image)
        smooth_img = imread('../image/smooth.png')
        self.show_image(self.lblImage_2, smooth_img)

    def sharp_image(self):
        import imageFilter as ifil
        from skimage.io import imread
        ifil.sharp_image(self.source_image)
        sharp_img = imread('../image/sharp.png')
        self.show_image(self.lblImage_2, sharp_img)

    def rotate_image(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.rotate_image(self.source_image)
        rotate_img = imread('../image/rotate.png')
        self.show_image(self.lblImage_2, rotate_img)

    def scaling_image(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.scaling_image(self.source_image)
        scaling_img = imread('../image/scaling.png')
        self.show_image(self.lblImage_2, scaling_img)

    def flip_image_left(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.flip_image_left(self.source_image)
        flip_left_img = imread('../image/flip_left_right.png')
        self.show_image(self.lblImage_2, flip_left_img)

    def flip_image_top(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.flip_image_top(self.source_image)
        flip_top_img = imread('../image/flip_top_bottom.png')
        self.show_image(self.lblImage_2, flip_top_img)

    def warp_image_row(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.warp_image_row(self.source_image)
        warp_row_img = imread('../image/warp_rows.png')
        self.show_image(self.lblImage_2, warp_row_img)

    def warp_image_col(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.warp_image_col(self.source_image)
        warp_col_img = imread('../image/warp_cols.png')
        self.show_image(self.lblImage_2, warp_col_img)

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