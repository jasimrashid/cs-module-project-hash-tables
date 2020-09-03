# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('ciphertext.txt', 'r') as f:
    words = f.read()


# STEPS
# 3: loop again. read each character and map it based on the mapping in step 1

# 1: loop through words, mapping each character to dictionary. sort by counts. then 
bad_chars = ('\n',' ','!','"','(',')',',','.','1',':',';','?','-') #'_'
char_count={}
for i in words:
    
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for i in bad_chars:
    char_count.pop(i)


char_count = dict(sorted(char_count.items(),key = lambda x: x[1], reverse=True))
char_count.pop("'")


# 2: create a cipher by mapping character frequency
with open('README.md', 'r') as f:
    readme = f.readlines()

char_frequency = []
for i in readme:
    if i[:2] == '| ':
        char_frequency.append(i[1:6].strip())

char_frequency.pop(0)

for a,b in zip(char_count, char_frequency):
    char_count[a] = b

# 3: decode characters in 'words' using cipher in step 2
for i in words:
    try:
        if i in bad_chars:
            print(i,end='')
        else:
            print(char_count[i],end='')
    except KeyError:
        continue