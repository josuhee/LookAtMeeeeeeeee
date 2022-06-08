# Final
# 201812245 Chang Jiyoung
# 201812433 Jo Suhee

from PyQt5.QtWidgets import QMainWindow

class multimedia_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        import videoIO as vio
        super(multimedia_processing_class, self).__init__()
        loadUi('../ui/final_project_app.ui', self)
        self.source_image = None
        self.video = vio.VideoIO()

        self.btnOpenimage.clicked.connect(lambda: self.open_image())

        self.btnToJPEG.clicked.connect(lambda: self.save_toJPEG())
        self.btnToPNG.clicked.connect(lambda: self.save_toPNG())
        self.btnToBMP.clicked.connect(lambda: self.save_toBMP())

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
        self.btnCropimage.clicked.connect(lambda: self.crop_image())

        self.btnOpenvideo.clicked.connect(lambda: self.open_video())
        self.btnConnectWebcam.clicked.connect(lambda: self.connectwebcam())
        self.btnStopWebcam.clicked.connect(lambda: self.stopwebcam())
        self.btnVideoConvert.clicked.connect(lambda: self.convertGray())

        self.btnVideoFlip_90.clicked.connect(lambda: self.rotate90())
        self.btnVideoFlip_180.clicked.connect(lambda: self.rotate180())
        self.btnVideoFlip_270.clicked.connect(lambda: self.rotate270())

    def open_image(self):
        import imageIO as iio
        self.source_image = iio.open_image(self.source_image)
        self.show_image(self.lblImage_1, self.source_image)

    def open_video(self):
        self.video.openVideo(self.lblVideo_1, self.lblVideo_2)

    def connectwebcam(self):
        self.video.connectwebcam(self.lblVideo_1, self.lblVideo_2)

    def stopwebcam(self):
        self.video.stopwebcam()

    def convertGray(self):
        self.video.convertGray()

    def rotate90(self):
        self.video.rotate90()

    def rotate180(self):
        self.video.rotate180()

    def rotate270(self):
        self.video.rotate270()

    def show_image(self, label, image):
        import imageIO as iio
        iio.show_image(label, image)

    def save_toJPEG(self):
        import imageIO as iio
        from skimage.io import imread
        iio.save_toJPEG(self.source_image)
        jpeg_img = imread('../image/toJPEG.jpeg')
        self.show_image(self.lblImage_2, jpeg_img)

    def save_toPNG(self):
        import imageIO as iio
        from skimage.io import imread
        iio.save_toPNG(self.source_image)
        png_img = imread('../image/toPNG.png')
        self.show_image(self.lblImage_2, png_img)

    def save_toBMP(self):
        import imageIO as iio
        from skimage.io import imread
        iio.save_toBMP(self.source_image)
        bmp_img = imread('../image/toBMP.bmp')
        self.show_image(self.lblImage_2, bmp_img)

    def show_histogram(self):
        import imageConvert01 as ic1
        from skimage.io import imread
        ic1.show_histogram(self.source_image)
        hist_img = imread('../image/hist.png')
        self.show_image(self.lblImage_2, hist_img)

    def invert_image(self):
        import imageConvert01 as ic1
        from skimage.io import imread
        a_max = float(self.txtAmax.toPlainText())
        ic1.invert_image(self.source_image, a_max)
        invert_img = imread('../image/invert.png')
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

    def crop_image(self):
        import imageConvert02 as ic2
        from skimage.io import imread
        ic2.crop_image(self.source_image)
        crop_img = imread('../image/crop.png')
        self.show_image(self.lblImage_2, crop_img)

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