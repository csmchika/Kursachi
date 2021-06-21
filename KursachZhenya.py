import sys  
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from cube import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Кручу куб, верчу - курсач сдать хочу')
        self.setWindowIcon(QIcon('icon.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
