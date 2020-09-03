# Your code here
import re

with open('robin.txt','r') as f:
    words = f.read()

words = words.split()


 
#1 strip out bad characters, convert to lower caseplace and then into dictionary, counting each word
word_counts = {}
# bad_words = 
# use a dictionary comprehension after tyring a for loop
for word in words:
    word = re.sub(": ; , . - + = / \ | [ ] { } ( ) * ^ & ","" , word).replace('"','').lower()
    if word in word_counts:
        word_counts[word] += 1

    else:
        # try:
        word_counts[word] = 1
        # except KeyError:
            # breakpoint()

#2 sort by count and by first inital descending (research this)
    # word_counts.sort()
word_counts = dict(sorted(word_counts.items()))
word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

# print(word_counts)


#3 display hashes. left justified
# print(word_counts)
for i,v in word_counts.items():
    spacing = 20
    print(i+' '*(spacing-len(i))+'#'*v)


# DO STRETCH: streamline bad_word strip. without regex
# QUESTION: are you allowed to impor regex
# STRETCH: unpack the encrypted hints