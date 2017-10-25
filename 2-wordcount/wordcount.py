excerpt = """
The Babel fish, said The Hitchhikers Guide to the Galaxy quietly,
is small, yellow, and leech-like, and probably the oddest thing in
the Universe. It feeds on brainwave energy received not from its own
carrier but from those around it. It absorbs all unconscious mental
frequencies from this brainwave energy to nourish itself with. It then
excretes into the mind of its carrier a telepathic matrix formed by
combining the conscious thought frequencies with nerve signals picked
up from the speech centres of the brain which has supplied them. The
practical upshot of all this is that if you stick a Babel fish in your
ear you can instantly understand anything said to you in any form of
language. The speech patterns you actually hear decode the brainwave
matrix which has been fed into your mind by your Babel fish.
"""

# Write a python program to print the three most common words from the
# text above

excerpt.strip()
#print(excerpt)

wordsList = excerpt.split()
#print(wordsList)
wordsList.sort()
#print(wordsList)

wordcounts = {}

for word in wordsList:
   lower_case_word = word.lower()
   try:
       wordcounts[lower_case_word]   = wordcounts[lower_case_word] + 1
   except KeyError:
       wordcounts[lower_case_word] = 1;
tuple_list = list(wordcounts.items())
#print wordcounts

def sort_by_count(name_tuple):
    return name_tuple[1]
tuple_list.sort(key=sort_by_count,reverse=True)
print tuple_list[:3]

    

