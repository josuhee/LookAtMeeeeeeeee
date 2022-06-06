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