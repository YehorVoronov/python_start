# 9:22:30 window + icon
# 9:31:30 labels

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowIcon(QIcon("/PYTHONLEARN/img/face.jpeg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color: green;"
        "background-color: #6fdcf7;"
        "font-weight: bold;"
        "font-style: italic;"
        "text-decoration: underline;")

        imgLabel = QLabel(self)
        imgLabel.setGeometry(0,0, 200, 200)

        pixmap = QPixmap("/PYTHONLEARN/img/face.jpeg")
        imgLabel.setPixmap(pixmap)

        imgLabel.setScaledContents(True)
        imgLabel.setGeometry((self.width() - imgLabel.width()) // 2,
        (self.height() - imgLabel.height()) // 2,
         imgLabel.width(), imgLabel.height())


        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignCenter)

        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: black;")

        # vbox = QVBoxLayout()
        # vbox = QHBoxLayout()
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
