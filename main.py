from PyQt6.QtWidgets import QApplication
from gui import Ui_MainWindow
from logic import VoteTracker
import sys


class Controller(Ui_MainWindow):
# connects GUI to voting logic
    def __init__(self):
        super().__init__()
        self.vote_tracker = VoteTracker()
        self.selected_candidate = None
        self.connect_buttons()

    def connect_buttons(self) -> None:
# connect button clicks to logic
        self.bianca_button.clicked.connect(lambda: self.select_candidate("Bianca"))
        self.edward_button.clicked.connect(lambda: self.select_candidate("Edward"))
        self.felicia_button.clicked.connect(lambda: self.select_candidate("Felicia"))
        self.submit_button.clicked.connect(self.submit_vote)

    def select_candidate(self, candidate: str) -> None:
# mark a candidate as selected
        self.selected_candidate = candidate
        self.results_label.setText(f"Selected: {candidate}")

    def submit_vote(self) -> None:
# handle vote submission with validation
        voter_id = self.voter_id_input.text().strip()
        if not voter_id:
            self.results_label.setText("Please enter a Voter ID.")
            return
        if not self.selected_candidate:
            self.results_label.setText("Please select a candidate.")
            return
        if self.vote_tracker.has_voted(voter_id):
            self.results_label.setText("You already voted.")
            return

        success = self.vote_tracker.vote(voter_id, self.selected_candidate)
        if success:
            results = self.vote_tracker.get_results()
            formatted_results = []
            for k, v in results.items():
                formatted_results.append(f"{k}: {v}")
            results_text = " | ".join(formatted_results)
            self.results_label.setText(results_text)
        else:
            self.results_label.setText("Voting failed. Try again.")


def main() -> None:
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
