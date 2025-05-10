import csv
import os

class VoteTracker:
# tracks votes for each candidate and prevents duplicate voting

    def __init__(self, filename: str = "votes.csv"):
        self._votes = {'Bianca': 0, 'Edward': 0, 'Felicia': 0}
        self._voted_ids = set()
        self._filename = filename
        self._load_data()

    def _load_data(self) -> None:
# load votes and voter IDs from file
        if not os.path.exists(self._filename):
            return
        try:
            with open(self._filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        voter_id, candidate = row
                        self._voted_ids.add(voter_id)
                        if candidate in self._votes:
                            self._votes[candidate] += 1
        except Exception as e:
            print(f"Error loading vote data: {e}")

    def _save_vote(self, voter_id: str, candidate: str) -> None:
# append a vote to the file
        try:
            with open(self._filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])
        except Exception as e:
            print(f"Error saving vote: {e}")

    def has_voted(self, voter_id: str) -> bool:
# check if the voter has already voted
        return voter_id in self._voted_ids

    def vote(self, voter_id: str, candidate: str) -> bool:
# register a vote if not already voted
        if self.has_voted(voter_id):
            return False
        if candidate in self._votes:
            self._votes[candidate] += 1
            self._voted_ids.add(voter_id)
            self._save_vote(voter_id, candidate)
            return True
        return False

    def get_results(self) -> dict:
# return the current vote counts
        total = sum(self._votes.values())
        return {**self._votes, 'Total': total}
