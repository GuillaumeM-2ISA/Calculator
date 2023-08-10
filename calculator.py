import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from calculator_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(self.writeButton1)
        self.ui.pushButton_8.clicked.connect(self.writeButton2)
        self.ui.pushButton_9.clicked.connect(self.writeButton3)
        self.ui.pushButton_4.clicked.connect(self.writeButton4)
        self.ui.pushButton_5.clicked.connect(self.writeButton5)
        self.ui.pushButton_7.clicked.connect(self.writeButton6)
        self.ui.pushButton_3.clicked.connect(self.writeButton7)
        self.ui.pushButton_2.clicked.connect(self.writeButton8)
        self.ui.pushButton.clicked.connect(self.writeButton9)
        self.ui.pushButton_10.clicked.connect(self.writeButton0)

        self.iscomma = False
        self.ui.pushButton_11.clicked.connect(self.writeButtonVirgule)
        self.ui.pushButton_12.clicked.connect(self.writeButtonDEL)

        self.ui.pushButton_13.clicked.connect(self.addition)
        self.ui.pushButton_14.clicked.connect(self.soustraction)
        self.ui.pushButton_15.clicked.connect(self.multiplication)
        self.ui.pushButton_16.clicked.connect(self.division)
        self.ui.pushButton_17.clicked.connect(self.egal)

    def writeButton1(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_6.text())

    def writeButton2(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_8.text())

    def writeButton3(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_9.text())

    def writeButton4(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_4.text())

    def writeButton5(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_5.text())

    def writeButton6(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_7.text())

    def writeButton7(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_3.text())

    def writeButton8(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_2.text())

    def writeButton9(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton.text())

    def writeButton0(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text + self.ui.pushButton_10.text())

    def writeButtonVirgule(self):
        text = self.ui.lineEdit.text()
        if len(text) != 0 and self.iscomma == False:
            self.ui.lineEdit.setText(text + self.ui.pushButton_11.text())
            self.iscomma = True

    def writeButtonDEL(self):
        text = self.ui.lineEdit.text()
        newtext = text.rstrip(text[-1])
        self.ui.lineEdit.setText(newtext)
        if text[-1] == ",":
            self.iscomma = False

    def addition(self):
        operande = self.ui.lineEdit.text()
        operateur = "+"
        self.ui.lineEdit.setText(operande + operateur)
        self.iscomma = False

    def soustraction(self):
        operande = self.ui.lineEdit.text()
        operateur = "-"
        self.ui.lineEdit.setText(operande + operateur)
        self.iscomma = False

    def multiplication(self):
        operande = self.ui.lineEdit.text()
        operateur = "*"
        self.ui.lineEdit.setText(operande + operateur)
        self.iscomma = False

    def division(self):
        operande = self.ui.lineEdit.text()
        operateur = "/"
        self.ui.lineEdit.setText(operande + operateur)
        self.iscomma = False

    def egal(self):
        res = eval(self.ui.lineEdit.text())
        print(res)
        self.ui.lineEdit.setText(str(res))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())