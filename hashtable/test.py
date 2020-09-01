# a  = 'a'
key = 'a'
b = key.encode()
# y = b.encode()

# print(x)
# for i in x:
#     print(i)
# print(type(x))
fnv_prime = 1099511628211
fnv_offset_basis = 14695981039346656037

hash_value = fnv_offset_basis
for i in b:
    hash_value = hash_value ^ i
    hash_value = hash_value * fnv_prime

print(hash_value)
