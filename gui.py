from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    """GUI for the Voting Application using PyQt6."""
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

    def setup_ui(self, MainWindow: QMainWindow) -> None:
        """Initialize the GUI layout."""
        MainWindow.setObjectName("CIS")
        MainWindow.resize(496, 589)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.voter_id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.voter_id_input.setGeometry(QtCore.QRect(10, 50, 471, 31))
        self.voter_id_input.setObjectName("voter_id_input")

        self.header_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(10, 0, 471, 31))
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")

        self.voter_id_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.voter_id_label.setGeometry(QtCore.QRect(10, 20, 471, 31))
        self.voter_id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.voter_id_label.setObjectName("voter_id_label")

        self.candidate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidate_label.setGeometry(QtCore.QRect(10, 90, 471, 31))
        self.candidate_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.candidate_label.setObjectName("candidate_label")

        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(20, 410, 451, 32))
        self.submit_button.setObjectName("submit_button")

        self.results_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.results_text.setGeometry(QtCore.QRect(10, 460, 151, 31))
        self.results_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.results_text.setObjectName("results_text")

        self.results_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.results_label.setGeometry(QtCore.QRect(210, 450, 251, 51))
        self.results_label.setObjectName("results_label")

        self.layout_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layout_widget.setGeometry(QtCore.QRect(10, 130, 471, 261))
        self.layout_widget.setObjectName("layout_widget")

        self.horizontal_layout = QtWidgets.QHBoxLayout(self.layout_widget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)

        self.bianca_button = QtWidgets.QPushButton(parent=self.layout_widget)
        self.edward_button = QtWidgets.QPushButton(parent=self.layout_widget)
        self.felicia_button = QtWidgets.QPushButton(parent=self.layout_widget)

        for btn, name in [(self.bianca_button, "Bianca"),
                          (self.edward_button, "Edward"),
                          (self.felicia_button, "Felicia")]:
            btn.setText(name)
            btn.setObjectName(f"{name.lower()}_button")
            self.horizontal_layout.addWidget(btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow: QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting App"))
        self.header_label.setText(_translate("MainWindow", "VOTING MENU"))
        self.voter_id_label.setText(_translate("MainWindow", "Enter Voter ID:"))
        self.candidate_label.setText(_translate("MainWindow", "Candidates (Pick One)"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.results_text.setText(_translate("MainWindow", "Results"))
        self.results_label.setText(_translate("MainWindow", "No votes yet"))
