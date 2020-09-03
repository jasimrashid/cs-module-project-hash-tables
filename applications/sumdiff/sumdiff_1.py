"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
from pprint import pprint

#q = set(range(1, 10))
q = set(range(1, 80))
# print(q)
# q = (1, 3, 4, 7, 12)
# print(q)
q = list(q)

# breakpoint()


# TODO: cache this?
print(q)
# f = {}
def f(x):
    return x * 4 + 6

def pad(x):
    return (3-len(str(x)))*'0'+str(x)


dict_lhs = {}
# Your code here
i = 0
j = 1
gap = 1
while i < len(q)-1:
    while j < len(q):
        # print(i,j, gap)
        x = (3-len(str(i)))*'0'+str(i)
        # key1 = pad(i)+'-'+pad(j)
        # key2 = pad(j)+'-'+pad(i)

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

            
# pprint(dict_lhs)

dict_rhs = {}
# Your code here
i = 0
j = 1
gap = 1
while i < len(q)-1:
    while j < len(q):
        # print(i,j, gap)
        # key3 = pad(i)+'-'+pad(j)
        # key4 = pad(j)+'-'+pad(i)
        key3 = str(i)+'-'+str(j)
        key4 = str(j)+'-'+str(i)
        # diff_3 = f(q[i]) - f(q[j])
        # diff_4 = f(q[j]) - f(q[i])
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key3 not in dict_rhs:# and key4 not in dict_rhs:
            dict_rhs[key3] = f(q[i]) - f(q[j])
        if key4 not in dict_rhs:    
            dict_rhs[key4] = abs(f(q[i]) - f(q[j]))

        

        i += 1
        j += 1
    gap += 1
    i = 0 if gap < len(q) else len(q)
    j = gap + i 

            
# pprint(dict_rhs)

# for key_l,value_l in dict_lhs.items():
#     # breakpoint()
    
#     a = int(key_l[:1])
#     b = int(key_l[2:3])
#     a_or_b = [a,b]
#     # print(a,b, a_or_b)

#     for key_r, value_r in dict_rhs.items():
#         c = int(key_r[:1])
#         d = int(key_r[2:3])
#         # print(c,d)
#         # if c not in a_or_b and d not in a_or_b:
#         #     print(value_l,value_r)
#         #     if value_l == value_r:
#         #         print("f({q[a]}) + f({q[b]} = f){q[c]} - f({q[d]})")
#         if value_l == value_r:

combined = {}
# Your code here
i = 0
j = 1
gap = 1
keys = [i for i in dict_lhs.keys()]

while i < len(dict_lhs)-1:
    while j < len(dict_lhs):
        # print(i,j, gap)
        key = keys[i]+'-'+keys[j]
        # key2 = keys[j]+'-'+keys[i]
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key not in combined:
            # breakpoint()
            combined[key] = dict_lhs[keys[i]] - dict_rhs[keys[j]]
            # combined[key2] = dict_lhs[key2] + dict_rhs[key2]

        # if either key is in the dictionary, then lookup the value from dictionary and populate the sum ans assign to the empty
        # elif key1 not in dict_lhs or key2 in dict_lhs:
        #     combined[key1] = combined[key2]

        # elif key1 in dict_lhs or key2 not in dict_lhs:
        #     combined[key2] = combined[key1]

        else:
            continue

        i += 1
        j += 1
        
    gap += 1
    i = 0 if gap < len(dict_lhs) else len(dict_lhs)
    j = gap + i 

        
# print('*** combined')
# pprint(combined)


# print('zippp')
# combined = {}
# for (k_l, v_l), (k_r, v_r) in zip(dict_lhs.items(), dict_rhs.items()):
#     # combining both lhs and rhs, but keeping the same name
#     print(k_l, k_r)
#     print(v_l, v_r)
#     combined[k_l+'-'+k_r] = v_l - v_r

# make this a list comprehension
combined_f = {}
for key,val in combined.items():
    if val == 0:
        # breakpoint()
        # a = int(key[0:1]) #LOGIC WILL FAIL FOR SIZE > 10!!!! PAD INDICES
        # b = int(key[2:3])
        # c = int(key[4:5])
        # d = int(key[6:7])
        pos = key.split('-')
        # breakpoint()
        # print('**', key,val)
        print(f"f({q[int(pos[0])]}) + f({q[int(pos[1])]}) = f({q[int(pos[2])]}) - f({q[int(pos[3])]})    {f(q[int(pos[0])])} + {f(q[int(pos[1])])} = {f(q[int(pos[2])])} - {f(q[int(pos[3])])}")
        # combined_f[key] = val

# print('combined')
# pprint(combined)


        
# breakpoint()


# if neither key is in the dictionary, then compute f(i) + f(j)

# elseit 
    # pair-up i and i+1; slide right O(n)

    # pair-up i and i+2; slide right O(n)

    # pair-up i and i+3; slide right O(n)