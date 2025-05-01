import sys

from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseWindow = uic.loadUiType("add_league_dialog.ui")

class AddLeagueDialogue(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AddLeagueDialogue()
    window.show()
    sys.exit(app.exec_())
