import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import subprocess

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ورود به PyCharm با PyQt6")
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton("ورود به PyCharm", self)
        button.setGeometry(150, 150, 150, 50)
        button.clicked.connect(self.open_pycharm)

    def open_pycharm(self):
        try:
            # دستور باز کردن PyCharm در اینجا قرار گرفته است.
            # ممکن است مسیر اجرای PyCharm بر اساس سیستم شما متفاوت باشد.
            subprocess.run(["pycharm"])
        except Exception as e:
            print(f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()