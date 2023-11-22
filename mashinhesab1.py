import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # ایجاد ویجت‌ها
        self.result_line = QLineEdit(self)
        self.result_line.setReadOnly(True)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # ایجاد یک دسته‌بندی برای دکمه‌ها
        grid_layout = QGridLayout()

        # افزودن دکمه‌ها به دسته‌بندی
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(self.button_click)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # ایجاد لایه اصلی
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_line)
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

        self.setWindowTitle('ماشین حساب')
        self.show()

    def button_click(self):
        # در اینجا عملیات کلیک دکمه محاسبه می‌شود
        button = self.sender()
        current_text = self.result_line.text()

        if button.text() == '=':
            try:
                result = eval(current_text)
                self.result_line.setText(str(result))
            except Exception as e:
                self.result_line.setText('Error')
        else:
            self.result_line.setText(current_text + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())