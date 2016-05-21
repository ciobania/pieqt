import sys
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QApplication,
                             QInputDialog)


class Fire(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton('fire', self)
        button.move(50, 50)
        button.clicked.connect(self.btn_click)

        self.setWindowTitle('Fire App')

        self.resize(250, 150)
        self.move(300, 300)
        self.show()

    def btn_click(self):
        print('Clicked button fire')
        text, ok = QInputDialog.getText(None, 'Name', 'Enter your name:')
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fire = Fire()

    sys.exit(app.exec_())
