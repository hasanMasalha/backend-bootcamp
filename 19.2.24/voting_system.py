class Candidate:
    def __init__(self, name, position={}):
        self.name = name
        self.position = position

    def add_votes(self, pos):
        if pos in self.position:
            self.position[pos] += 1

class Vote:
    def __init__(self, id, for_candidate, pos):
        self.id = id
        self.for_candidate = for_candidate
        self.pos = pos

class Voter:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.votes = {}

    def vote_for_candidate(self, candidate, pos):
        if pos in candidate.position:
            if pos not in self.votes:
                candidate.add_votes(pos)
                self.votes[pos] = candidate

voters = []

for i in range(1, 21):
    name = f"Person{i}"
    age = 20 + i  # Assigning arbitrary ages for demonstration
    addr = f"Address{i}"
    
    voter = {"name": name, "age": age, "addr": addr}
    voters.append(voter)




    candidate1 = Candidate("Candidate1", {"Prime Minister": 0, "Minister": 0, "President": 0})
    candidate2 = Candidate("Candidate2", {"Prime Minister": 0, "Minister": 0, "President": 0})

    voter1 = Voter("Voter1", 25, "Address1")

    voter1.vote_for_candidate(candidate1, "Prime Minister")
    voter1.vote_for_candidate(candidate2, "President")

    # Displaying votes and candidate positions
    print("Votes from Voter1:")
    for pos, candidate in voter1.votes.items():
        print(f"{voter1.name} voted for {candidate.name} for {pos}")

    print("\nCurrent positions and votes for candidates:")
    for pos, count in candidate1.position.items():
        print(f"{candidate1.name} for {pos}: {count} votes")

    for pos, count in candidate2.position.items():
        print(f"{candidate2.name} for {pos}: {count} votes")
