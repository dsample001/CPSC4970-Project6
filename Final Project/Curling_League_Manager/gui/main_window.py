import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pyqt5_plugins.examplebutton import QtWidgets

from Curling_League_Manager.gui.add_league_dialogue import AddLeagueDialogue
from Curling_League_Manager.model.league import League
from Curling_League_Manager.model.league_database import LeagueDatabase

Ui_MainWindow, QtBaseWindow = uic.loadUiType('main_window.ui')



class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._ld = LeagueDatabase()
        # Menu Items
        self.action_open_league.triggered.connect(self.action_open_league_triggered)
        self.action_save_league.triggered.connect(self.action_save_league_triggered)
        self.action_import_league_csv.triggered.connect(self.action_import_league_csv_triggered)
        self.action_export_league_csv.triggered.connect(self.action_export_league_csv_triggered)
        self.action_quit.triggered.connect(self.action_quit_triggered)
        # Buttons
        self.add_league_button.clicked.connect(self.add_league_button_clicked)
        self.rename_league_button.clicked.connect(self.rename_league_button_clicked)
        self.edit_league_teams_button.clicked.connect(self.edit_league_teams_button_clicked)
        self.edit_league_comp_button.clicked.connect(self.edit_league_comp_button_clicked)


    def update_ui(self):
        if len(self._ld.leagues) > 0:
            for l in self._ld.leagues:
                self.league_list_widget.addItem(l.name)
        else:
            self.league_list_widget.addItem("No Leagues")

    # Menu selections.
    def action_open_league_triggered(self):
        fname = QFileDialog.getOpenFileName(self, "Open League", "", "DAT File (*.dat);;All Files (*)")
        if fname:
            self.label.setText(fname[0])
            LeagueDatabase.load(fname[0])
            self.update_ui()


    def action_save_league_triggered(self):
        mb = QMessageBox(QMessageBox.Icon.Critical, "Ouch", "Save League Selected")
        mb.exec()

    def action_import_league_csv_triggered(self):
        fname = QFileDialog.getOpenFileName(self, "Import League CSV", "", "CSV File (*.csv);;All Files (*)")
        if fname:
            self.label.setText(fname[0])
            ld = LeagueDatabase()
            new_league = League(ld.next_oid(), "New League")
            ld.import_league_teams(new_league, fname[0])

    def action_export_league_csv_triggered(self):
        mb = QMessageBox(QMessageBox.Icon.Critical, "Ouch", "Export League CSV Selected")
        mb.exec()

    def action_quit_triggered(self):
        dialog = QMessageBox(QMessageBox.Icon.Question,
                             "Are you sure?",
                             "Are you sure that you want to close application?",
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            sys.exit()

    def add_league_button_clicked(self):
        dialog = AddLeagueDialogue()
        dialog.acceptied.connect(lambda: self.add_laague_accepted(dialog))
        dialog.show()

    def add_league_accepted(self, dialog):
        print("Adding League")

    def rename_league_button_clicked(self):
        pass

    def edit_league_teams_button_clicked(self):
        pass

    def edit_league_comp_button_clicked(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
