import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

# 1: parse words -> turn into dictionary with follow words

words = words.split()

# print(words)

dictionary = {}
for pos,word in enumerate(words[:-1]):
    if word not in dictionary:
        dictionary[word] = [words[pos+1]] #index error for last line will be caught below 
    else: # else, whe word in in the dictionary, append the word following it to list
        dictionary[word].append(words[pos+1])

# print(dictionary)






# TODO: construct 5 random sentences
# loop through 5 times. pick a random word. is it a start word? no-> repeat until
# it is a start word. print start word. (repeat point) pick and print random next word. if it is a stop
# word, stop. else, repeat.

sentences = 0
while sentences != 6:
    
    start_word = None
    while start_word is None:
        word_pos = random.randint(0,len(words)-1)
        # if is a start word?
        if words[word_pos][:1].isupper() or (words[:1] == '"' and words[1:2].isupper()):
            start_word = words[word_pos]
    print(start_word, end=' ')

    next_word = random.choice(dictionary[start_word])
    print(next_word, end = ' ')

    stop_word = None
    while stop_word is None:
        if next_word[-1:] in ('?','!','.'):
            stop_word = next_word
            sentences += 1
            print()
        else:
            try:
                next_word = random.choice(dictionary[next_word])
                print(next_word, end = ' ')
            except KeyError:
                # breakpoint()
                print('exception: solve this shit!')
                # print('exception: ',next_word)

        


