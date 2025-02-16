from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setStyleSheet("background-color: #121212; color: #39ff14;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 380, 50))
        self.display.setStyleSheet("background-color: black; color: #39ff14; font-size: 20px;")
        self.display.setObjectName("display")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 380, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        button_names = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('sin', 4, 1), ('cos', 4, 2), ('tan', 4, 3),
            ('log', 5, 0), ('sqrt', 5, 1)
        ]
        
        self.buttons = {}
        for text, row, col in button_names:
            self.buttons[text] = QtWidgets.QPushButton(self.gridLayoutWidget)
            self.buttons[text].setText(text)
            self.buttons[text].setStyleSheet("background-color: #1e1e1e; color: #39ff14; border: 2px solid red; font-size: 16px;")
            self.gridLayout.addWidget(self.buttons[text], row, col)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator"))
