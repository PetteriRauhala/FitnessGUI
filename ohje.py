# HELP DIALOG WINDOW    
# ==================

# Libraries and modules
from PyQt5 import QtWidgets as QW # Ui elements functionality
from PyQt5.uic import loadUi # Reads the UI file

# Class definition
class OpenHelp(QW.QDialog):

    # The constructor
    def __init__(self):
        super().__init__()

        loadUi('ohje.ui', self)
        self.setWindowTitle('Kuntoilusovelluksen ohje')
        self.closePB = self.closePushButton
        self.closePB.clicked.connect(self.closeHelp)

    # Methods ie. slots
    def closeHelp(self):
        self.close()

