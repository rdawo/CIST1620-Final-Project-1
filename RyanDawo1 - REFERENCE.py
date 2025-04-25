def vote_menu():
    print('----------------------------------')
    print('VOTE MENU')
    print('----------------------------------')
    print('v: Vote')
    print('x: Exit')

    while True:
        option = input('Option: ').strip().lower()
        if option in  ('v', 'x'):
            return option
        else:
            print("Invalid (v/x): ", end='')


def candidate_menu():
    print('----------------------------------')
    print('CANDIDATE MENU')
    print('----------------------------------')
    print('1: Bianca')
    print('2: Edward')
    print('3: Felicia')

    while True:
        candidate = input('Candidate: ').strip()
        if candidate.isdigit() and int(candidate) in (1, 2, 3):
            return int(candidate)
        else:
            print("Invalid (1/2/3): ", end='')


def main():
    votes = {'Bianca': 0, 'Edward': 0, 'Felicia': 0}
    candidates = {1: 'Bianca', 2: 'Edward', 3: 'Felicia'}

    while True:
        vote_status = vote_menu()
        if vote_status == 'x':
            break

        selected_candidate = candidate_menu()
        candidate_name = candidates[selected_candidate]
        votes[candidate_name] += 1
        print(f"Voted {candidate_name}")
    total_votes = sum(votes.values())
    print('-------------------------------------------------------')
    print(
        f"Bianca – {votes['Bianca']}, Edward – {votes['Edward']}, Felicia – {votes['Felicia']}, Total – {total_votes}")
    print('-------------------------------------------------------')


# Run the program
if __name__ == "__main__":
    main()