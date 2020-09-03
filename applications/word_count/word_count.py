def word_count(s):
    wc = {}
    

# without splitting string 

    words_list = s.split()
    bad_chars = [":",";",",", ".", "-", "+", "=", "/", "|", "[","]", "{", "}", "(", ")", "*", "^", "&",'"'] 
    for i in words_list:
        word = "".join([j.lower() for j in i if j not in bad_chars]).replace("\\","")
        # word = None if word == "" else word
        if word == "":
            continue
        elif word not in wc:
            wc[word] = 1
        else:
            wc[word] += 1



    return wc

        
if __name__ == "__main__":
    # print(word_count('hello'))
    # print(word_count('hello world hello'))
    # print(word_count(' hello world'))
    # print(word_count(' hello, world a '))
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))