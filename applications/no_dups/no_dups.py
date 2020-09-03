def no_dups(s):
    # Your code here
    output_string = ""
    word_count = {}
    i = 0
    word = ''

    # word = ''
    for i, c in enumerate(s):
        if i == len(s)-1:
            word += c
            if word not in word_count:
                word_count[word] = 1
                output_string += word
            # else:
            #     output_string += word
            
        elif c == " ":
            if word not in word_count:
                word_count[word] = 1
                output_string += word + ' '
            # else:
            #     output_string += word
            word = ''
        else:
            word += c
       
    return output_string.strip()




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))