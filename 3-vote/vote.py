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
