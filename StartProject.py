import sys
import main
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main.main()
    sys.exit(app.exec_())
