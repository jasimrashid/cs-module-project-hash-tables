"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import time
from pprint import pprint

#q = set(range(1, 10))
q = set(range(1, 10)) #.016s
# print(q)
# q = (1, 3, 4, 7, 12) #.0001s
# print(q)
q = list(q)

# print(q)
# f = {}
def f(x):
    return x * 4 + 6

def pad(x):
    return (3-len(str(x)))*'0'+str(x)

dict_lhs = {}

time1 = time.time()
for i in range(len(q)):
    for j in range(len(q)):
        key1 = str(i)+'-'+str(j)
        key2 = str(j)+'-'+str(i)
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key1 not in dict_lhs and key2 not in dict_lhs:
            dict_lhs[key1] = f(q[i]) + f(q[j])
            dict_lhs[key2] = f(q[i]) + f(q[j])
        elif key1 not in dict_lhs or key2 in dict_lhs:
            dict_lhs[key1] = dict_lhs[key2]
        elif key1 in dict_lhs or key2 not in dict_lhs:
            dict_lhs[key2] = dict_lhs[key1]

        else:
            continue
time2 = time.time()
print('interval 1:', time2 - time1)

dict_rhs = {}
for i in range(len(q)):
    for j in range(len(q)):
        key3 = str(i)+'-'+str(j)
        key4 = str(j)+'-'+str(i)
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key3 not in dict_rhs:# and key4 not in dict_rhs:
            dict_rhs[key3] = f(q[i]) - f(q[j])
        if key4 not in dict_rhs:    
            dict_rhs[key4] = abs(f(q[i]) - f(q[j]))


# pprint(dict_rhs)
time3 = time.time()
print('interval 2:', time3 - time2)


combined = {}
# print(dict_lhs)
# filtered_dict = {k:v for k,v in d.iteritems() if filter_string in k}
# dict_rhs = {k:v for (k,v) in dict_rhs.items() if v >= 0}
# print(dict_rhs)
# breakpoint()

keys = [i for i in dict_lhs.keys()]
time3_1 = time.time()
print('interval 3_1:', time3_1 - time3)
# print('i')
# for i,vi in dict_lhs.items():
#     print(i)
# print('j')
# for j,vj in dict_rhs.items():
#     print(j)

    
print(len(dict_rhs), len(dict_lhs))
# print(keys)
for i in range(len(dict_lhs)):
    for j in range(len(dict_lhs)):        # print(i,j, gap)
# for i,vi in dict_lhs.items():
#     for j,vj in dict_rhs.items():
        # breakpoint()
        key = keys[i]+'-'+keys[j]
        # if neither key is in the dictionary, then compute f(i) + f(j). then create 2 entries in the mappign table
        if key not in combined:
            try:
                combined[key] = dict_lhs[keys[i]] - dict_rhs[keys[j]]
            except KeyError:
                breakpoint()
time4 = time.time()
print('interval 3:', time4 - time3)
# print(combined)       
for key,val in combined.items():
    if val == 0:
        pos = key.split('-')
        print(f"f({q[int(pos[0])]}) + f({q[int(pos[1])]}) = f({q[int(pos[2])]}) - f({q[int(pos[3])]})    {f(q[int(pos[0])])} + {f(q[int(pos[1])])} = {f(q[int(pos[2])])} - {f(q[int(pos[3])])}")

time5 = time.time()
print('interval 4:', time5 - time4)

# print('interval 4:', time2 - time1)


# 20
"""
20
interval 1: 0.0006260871887207031
interval 2: 0.0007259845733642578
interval 3: 0.08324503898620605
interval 4: 0.010164022445678711

30

interval 1: 0.0014736652374267578
interval 2: 0.0014641284942626953
interval 3: 0.48996615409851074
interval 4: 0.05346083641052246

40
interval 1: 0.0026209354400634766
interval 2: 0.0025720596313476562
interval 3: 1.6154286861419678
interval 4: 0.17033910751342773



"""


