import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mBoxLayoutMain = QVBoxLayout()

        #QPushButton(버튼 텍스트, self)
        mButtonDrinkA = QPushButton('음료A \n\n1000원\n\n재고 없음', self)
        mButtonDrinkB = QPushButton('음료B', self)
        mButtonDrinkC = QPushButton('음료C', self)
        mButtonDrinkD = QPushButton('음료D', self)
        mButtonDrinkE = QPushButton('음료E', self)
        mButtonDrinkF = QPushButton('음료F', self)
        mButtonDrinkG = QPushButton('음료G', self)
        mButtonDrinkH = QPushButton('음료H', self)
        mButtonSide1 = QPushButton('메뉴1', self)
        mButtonSide2 = QPushButton('메뉴2', self)
        mButtonPay = QPushButton('결제하기', self)

        #setGeometry(X좌표, Y좌표, X길이, Y길이)
        mButtonDrinkA.setGeometry(100, 150, 200, 200)
        mButtonDrinkB.setGeometry(350, 150, 200, 200)
        mButtonDrinkC.setGeometry(100, 400, 200, 200)
        mButtonDrinkD.setGeometry(350, 400, 200, 200)
        mButtonDrinkE.setGeometry(100, 650, 200, 200)
        mButtonDrinkF.setGeometry(350, 650, 200, 200)
        mButtonDrinkG.setGeometry(100, 900, 200, 200)
        mButtonDrinkH.setGeometry(350, 900, 200, 200)
        mButtonSide1.setGeometry(650, 150, 100, 300)
        mButtonSide2.setGeometry(650, 450, 100, 300)
        mButtonPay.setGeometry(650, 800, 100, 300)

        #addWidget(버튼ID)
        mBoxLayoutMain.addWidget(mButtonDrinkA)
        mBoxLayoutMain.addWidget(mButtonDrinkB)
        mBoxLayoutMain.addWidget(mButtonDrinkC)
        mBoxLayoutMain.addWidget(mButtonDrinkD)
        mBoxLayoutMain.addWidget(mButtonDrinkE)
        mBoxLayoutMain.addWidget(mButtonDrinkF)
        mBoxLayoutMain.addWidget(mButtonDrinkG)
        mBoxLayoutMain.addWidget(mButtonDrinkH)
        mBoxLayoutMain.addWidget(mButtonSide1)
        mBoxLayoutMain.addWidget(mButtonSide2)
        mBoxLayoutMain.addWidget(mButtonPay)

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('src\icon.png'))
        self.setGeometry(300, 300, 750, 1200)
        self.center()
        self.show()

    def center(self):
        svm = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        svm.moveCenter(center)
        self.move(svm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
