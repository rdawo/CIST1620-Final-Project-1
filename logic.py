# logic.py
class VoteTracker:
    def __init__(self):
        self.votes = {'Bianca': 0, 'Edward': 0, 'Felicia': 0}
        self.voted_ids = set()

    def has_voted(self, voter_id):
        return voter_id in self.voted_ids

    def vote(self, voter_id, candidate_name):
        if voter_id in self.voted_ids:
            return False  # Already voted

        if candidate_name in self.votes:
            self.votes[candidate_name] += 1
            self.voted_ids.add(voter_id)
            return True
        return False

    def get_results(self):
        total = sum(self.votes.values())
        return {**self.votes, 'Total': total}
