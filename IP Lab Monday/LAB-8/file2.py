''' 
Given a text file having regular text from a novel. 
Write a program that user can use to find out how many times a word has been used in this text. 
Also, write in another file, the top 10 most frequent words. 
You should create a dictionary of words with frequency as the value.
'''

with open("novel.txt") as f:
    words = []
    for line in f:
        for c in (line.strip()).split():
            words += [(c.lower()).strip('.,"'';?\/:!@#$%^&*()-+=[]{}|<>`~')]

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_freq = sorted(
    freq.items(), key=lambda x: x[1], reverse=True)

print("the words along with their frequencies in the form of a dictionary are as follows:")
print()
print(*sorted_freq)

with open('top_10_most_occuring.txt', 'w') as f:
    for word, count in sorted_freq[:10]:
        f.write(f'{word}: {count}\n')
