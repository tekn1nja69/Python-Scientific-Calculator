import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_MainWindow
import math

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        # Number buttons
        for i in range(10):
            getattr(self.ui, f'btn_{i}').clicked.connect(lambda _, x=i: self.add_to_display(str(x)))
        
        # Operator buttons
        self.ui.btn_add.clicked.connect(lambda: self.add_to_display('+'))
        self.ui.btn_subtract.clicked.connect(lambda: self.add_to_display('-'))
        self.ui.btn_multiply.clicked.connect(lambda: self.add_to_display('*'))
        self.ui.btn_divide.clicked.connect(lambda: self.add_to_display('/'))
        self.ui.btn_clear.clicked.connect(self.clear_display)
        self.ui.btn_equals.clicked.connect(self.calculate_result)
        
        # Scientific functions
        self.ui.btn_sin.clicked.connect(lambda: self.add_to_display('math.sin('))
        self.ui.btn_cos.clicked.connect(lambda: self.add_to_display('math.cos('))
        self.ui.btn_tan.clicked.connect(lambda: self.add_to_display('math.tan('))
        self.ui.btn_log.clicked.connect(lambda: self.add_to_display('math.log('))
        self.ui.btn_sqrt.clicked.connect(lambda: self.add_to_display('math.sqrt('))

    def add_to_display(self, value):
        self.ui.display.setText(self.ui.display.text() + value)

    def clear_display(self):
        self.ui.display.clear()

    def calculate_result(self):
        try:
            result = eval(self.ui.display.text(), {"math": math})
            self.ui.display.setText(str(result))
        except Exception:
            self.ui.display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
