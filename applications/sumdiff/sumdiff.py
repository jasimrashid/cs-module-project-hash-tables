"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


print(q)
def f(x):
    return x * 4 + 6

dict_lhs = {}
# Your code here
i = 0
j = 1
gap = 1
while i < len(q)-1:
    while j < len(q):
        print(i,j, gap)
        key1 = str(i)+'-'+str(j)
        key2 = str(j)+'-'+str(i)
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key1 not in dict_lhs and key2 not in dict_lhs:
            dict_lhs[key1] = f(q[i]) + f(q[j])
            dict_lhs[key2] = f(q[i]) + f(q[j])

        # if either key is in the dictionary, then lookup the value from dictionary and populate the sum ans assign to the empty
        elif key1 not in dict_lhs or key2 in dict_lhs:
            dict_lhs[key1] = dict_lhs[key2]

        elif key1 in dict_lhs or key2 not in dict_lhs:
            dict_lhs[key2] = dict_lhs[key1]

        else:
            continue

        i += 1
        j += 1
    gap += 1
    i = 0 if gap < len(q) else len(q)
    j = gap + i 

            
print(dict_lhs)

dict_rhs = {}
# Your code here
i = 0
j = 1
gap = 1
while i < len(q)-1:
    while j < len(q):
        print(i,j, gap)
        key3 = str(i)+'-'+str(j)
        key4 = str(j)+'-'+str(i)
        # diff_3 = f(q[i]) - f(q[j])
        # diff_4 = f(q[j]) - f(q[i])
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key3 not in dict_rhs:# and key4 not in dict_rhs:
            dict_rhs[key3] = f(q[i]) - f(q[j])
        if key4 not in dict_rhs:    
            dict_rhs[key4] = abs(f(q[i]) - f(q[j]))

        # elif key3 not in dict_rhs or key4 in dict_rhs:
        #     dict_rhs[key3] = dict_rhs[key4]

        # elif key3 in dict_rhs or key4 not in dict_rhs:
        #     dict_rhs[key4] = dict_rhs[key3]

        # else:
        #     continue

        # if key3 in dict_rhs:
        #     dict_rhs[key3] = 
        # if key3 not in dict_rhs or key4 in dict_rhs:
        #     dict_rhs[key3] = dict_rhs[key4]

        # if key3 in dict_rhs or key4 not in dict_rhs:
        #     dict_rhs[key3] = dict_rhs[key4]
        # else:
        #     continue

        i += 1
        j += 1
    gap += 1
    i = 0 if gap < len(q) else len(q)
    j = gap + i 

            
print(dict_rhs)
for key_l,value_l in dict_lhs.items():
    # breakpoint()
    
    a = int(key_l[:1])
    b = int(key_l[2:3])
    a_or_b = [a,b]
    # print(a,b, a_or_b)

    for key_r, value_r in dict_rhs.items():
        c = int(key_r[:1])
        d = int(key_r[2:3])
        # print(c,d)
        # if c not in a_or_b and d not in a_or_b:
        #     print(value_l,value_r)
        #     if value_l == value_r:
        #         print("f({q[a]}) + f({q[b]} = f){q[c]} - f({q[d]})")
        if value_l == value_r:
            print(f"f({q[a]}) + f({q[b]} = f){q[c]} - f({q[d]})")

        
# breakpoint()





# if neither key is in the dictionary, then compute f(i) + f(j)

# else
    # pair-up i and i+1; slide right O(n)

    # pair-up i and i+2; slide right O(n)

    # pair-up i and i+3; slide right O(n)