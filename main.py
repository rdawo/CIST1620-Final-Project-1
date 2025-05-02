import sys
from PyQt6.QtWidgets import +
from gui import Ui_MainWindow
from logic import VoteTracker


class VoteController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = VoteTracker()
        self.setup_connections()

    def setup_connections(self):
        self.ui.BiancaButton.clicked.connect(lambda: self.submit_vote('Bianca'))
        self.ui.EdwardButton.clicked.connect(lambda: self.submit_vote('Edward'))
        self.ui.FeliciaButton.clicked.connect(lambda: self.submit_vote('Felicia'))

    def submit_vote(self, candidate_name):
        voter_id = self.ui.IDNumber.text().strip()

        if not voter_id:
            self.ui.ResultsLabel.setText("Enter Voter ID.")
            return

        if self.model.has_voted(voter_id):
            self.ui.ResultsLabel.setText("This Voter ID has already voted.")
            return

        success = self.model.vote(voter_id, candidate_name)
        if success:
            results = self.model.get_results()
            results_str = (
                f"Bianca – {results['Bianca']}\n"
                f"Edward – {results['Edward']}\n"
                f"Felicia – {results['Felicia']}\n"
            )
            self.ui.ResultsLabel.setText(results_str)
        else:
            self.ui.ResultsLabel.setText("Error: Could not record vote.")

        self.ui.IDNumber.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoteController()
    window.show()
    sys.exit(app.exec())
