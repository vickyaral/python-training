
color_count = {}
already_voted = []

f = open("votes.txt")
for line in f:
   fields =  line.split('-')
   person = fields[0].lower().strip()
   if person not in already_voted:
               already_voted.append(person)
               color = fields[1].strip()
               color_count[color] =   color_count.get(color,0) + 1

def sort_by_count(color_tuple):
   return color_tuple[1]

count_list =  list(color_count.items())   
count_list.sort(key=sort_by_count,reverse=True)
print count_list[:1]
######3
votes = {}
voters = []


with open("votes.txt") as file_obj:
    for line in file_obj:
        person, vote = [item.strip() for item in line.split("-")]
        if person.lower() in voters:
            continue

        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
        voters.append(person.lower())

winner = ("", 0)
for colour in votes:
    if votes[colour] > winner[1]:
        winner = (colour, votes[colour])

print("Annnd, the winner is {0[0]} with {0[1]} votes!".format(winner))

