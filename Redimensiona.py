import sys
from design import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap


class Redimensiona(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_img)

    def abrir_img(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir arquivo',
            r'C:\Users\NOTE\Pictures',
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labeLImg.setPixmap(self.original_img)
        self.InputLargura.setText(str(self.original_img.width()))
        self.InputAltura.setText(str(self.original_img.height()))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Redimensiona()
    novo.show()
    qt.exec()
