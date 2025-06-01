import sys
from PyQt6.QtWidgets import QApplication
from gui import SchedulerApp


def main():
    app = QApplication(sys.argv)
    window = SchedulerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
