def word_count(s):
    wc = {}
    

# without splitting string 

    beg = 0

    c = ''
    word = ''
    word_count = {}
    for i,c in enumerate(s):
        # if character is end of line, then add the word to the dictionary
        if i ==  len(s)-1: #edge case what if there is a space at the end of line or special characters
            word += c.lower() if c not in [":",";",",", ".", "-", "+", "=", "/", "|", "[","]", "{", "}", "(", ")", "*", "^", "&",'"'] else c
            if word not in word_count:
                word_count[word] = 1
                word = ''
            else:
                word_count[word] += 1
                word = ''

        # if character is a whitespace, then add the word(concatenation of previous characters) to the dictionary
        elif c == ' ': 
            if word not in word_count:
                word_count[word] = 1
                word = ''
            else:
                word_count[word] += 1
                word = '' #reset word

        # if character is: " : ; , . - + = / \ | [ ] { } ( ) * ^ &, skip it
        elif c in [":",";",",", ".", "-", "+", "=", "/", "|", "[","]", "{", "}", "(", ")", "*", "^", "&",'"']: # \ and quotes are special special cases
            continue #this skips character
        else: #when character is part of word
            word += c.lower()

        print(i, c, word)
    return word_count

# edge cases  
# case 1: space in begninning / end "padding"
# case 2: weird special characters
# case 3: separate words with only punctuation in between but no spaces
# case 4: two spaces

        
if __name__ == "__main__":
    print(word_count('hello'))
    print(word_count('hello world hello'))
    print(word_count(' hello world'))
    print(word_count(' hello, world a '))
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('Hello      hello'))