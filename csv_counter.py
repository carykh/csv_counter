FILEPATH = "TPOT 17 Vote.csv"
indices_for_votes = [2,3] # The 2nd and 3rd columns are the ones to track (0-indexed)

def print_sorted(d):
    d_view = sorted( ((v,k) for k,v in d.items()), reverse=True)
    total = 0
    for v,k in d_view:
        print(f"{k}: {v} votes")
        total += v
    print("--------")
    print(f"Total: {total} votes")
    print("--------")
    print("")

f = open(FILEPATH, "r+")
lines = f.read().split("\n")[1:] # remove the header row
f.close()

for index in indices_for_votes:
    votes = {}
    for line in lines:
        parts = line.split(",")
        vote = parts[index].replace("\"","")
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    print_sorted(votes)
