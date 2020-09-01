class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = max(MIN_CAPACITY, capacity)
        self.length = 0
        self.list = [None]*self.capacity
        self.head = None
        self.tail = None
        
        
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity #is this true?


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def stupid_hash(self, key, capacity):
        b = key.encode()  # Get the bytes of the string
        total = 0
        for i in b:  # O(n) over the size of the key, O(1) over the size of the hash table
            total += i
        # return total % self.capacity
        return total % capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
    
        # Your code here
        # offset basis and FNVPriem are specially designated constants. 
        fnv_prime = 1099511628211
        fnv_offset_basis = 14695981039346656037

        hash_value = fnv_offset_basis
        for i in key.encode():
            hash_value = hash_value ^ i
            hash_value = hash_value * fnv_prime

        return hash_value % self.get_num_slots()


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # print()
        print('adding hash: ', 'key:', key, 'hash:',self.fnv1(key), 'value:',value, 'length:',self.length, 'capacity:',self.capacity)
        entry = HashTableEntry(key, value)

        if self.length == self.capacity:
            self.capacity += 1
            print('capacity reached')
            self.resize(self.capacity)
            self.tail.next = entry
            self.tail = entry
            # entry.next = self.head #
            # self.head = entry
            # self.list[self.stupid_hash(key)] = value
            self.list[self.fnv1(key)] = value
            # self.length += 1
            print(self.list, self.length, self.capacity, self.head.value, self.tail.value, self.tail.next is None)
        

        elif self.length == 0:
            self.list[self.fnv1(key)] = value
            self.length += 1
            self.head = entry
            self.tail = entry
            # print('1')

        else:
            self.tail.next = entry
            self.tail = entry
            self.list[self.fnv1(key)] = value
            self.length += 1
            # print('2')
        print('added hash:  ', 'key:', key, 'hash:',self.fnv1(key), 'value:',value, 'length:',self.length, 'capacity:',self.capacity)
            



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        # print('pre')
        # print(self.list, self.length, self.capacity, self.head.value, self.tail.value, self.tail.next is None)
        # self.capacity = new_capacity
        new_hash_table = HashTable(self.capacity+1)
        # new_hash_table.list = [None] * self.capacity
        # self.list = [None] * self.capacity
        # self.length = 0
        # print('mid')
        # print(self.list, self.capacity, self.length, self.head.value, self.tail.value, self.tail.next is None)
        

        current_entry = self.head
        # breakpoint()
        while current_entry:
            # new_hash = self.fnv1(current_entry.key)
            # new_hash = new_hash_table.fnv1(current_entry.key)
            # print(new_hash, current_entry.value,current_entry.next.value if current_entry.next is not None else '', current_entry.key)
            # self.list[self.fnv1(current_entry.key)] = current_entry.value
            # self.list[new_hash] = current_entry.value
            # new_hash_table.list[self.fnv1(current_entry.key)] = current_entry.value
            # self.list[new_hash] = current_entrly.value
            new_hash_table.put(current_entry.key, current_entry.value)
            current_entry = current_entry.next
            # self.length += 1

        self.head = new_hash_table.head
        self.tail = new_hash_table.tail
        self.length=  new_hash_table.length
        self.capacity = new_hash_table.capacity
        self.list = new_hash_table.list



        # print('post')
        # print(self.list, self.length, self.capacity, self.head.value, self.tail.value, self.tail.next is None, self.fnv1("line_10"),self.fnv1('line_9'))
        
        
            
            
        

if __name__ == "__main__":
    ht = HashTable(8)

    "line_ ", ht.put("line_1", "A")# 
    "line_ ", ht.put("line_2", "B")#
    "line_ ", ht.put("line_3", "C")#
    "line_ ", ht.put("line_4", "D")
    "line_ ", ht.put("line_5", "E"),
    "line_ ", ht.put("line_6", "F")
    "line_ ", ht.put("line_7", "G")
    "line_ ", ht.put("line_8", "H")
    "line_ ", ht.put("line_9", "I")
    "line_ ", ht.put("line_10", "J")
    "line_ ", ht.put("line_11", "K")
    "line_ ", ht.put("line_12", "L")
    # print("line_1 ", ht.fnv1("A"))
    # print("line_2 ", ht.fnv1("B"))
    # print("line_3 ", ht.fnv1("C"))
    # print("line_4 ", ht.fnv1("D"))
    # print("line_5 ", ht.fnv1("E"))
    # print("line_6 ", ht.fnv1("F"))
    # print("line_7 ", ht.fnv1("G"))
    # print("line_8 ", ht.fnv1("H"))
    # print("line_9 ", ht.fnv1("line_9"))
    # print("line_10 ", ht.fnv1("line_10"))
    # print("line_11 ", ht.fnv1("line_11"))
    # print("line_12 ", ht.fnv1("line_12"))
    # "line_ ", ht.put("line_1", "'Twas brillig, and the slithy toves")
    # "line_ ", ht.put("line_2", "Did gyre and gimble in the wabe:")
    # "line_ ", ht.put("line_3", "All mimsy were the borogoves,")
    # "line_ ", ht.put("line_4", "And the mome raths outgrabe.")
    # "line_ ", ht.put("line_5", '"Beware the Jabberwock, my son!')
    # "line_ ", ht.put("line_6", "The jaws that bite, the claws that catch!")
    # "line_ ", ht.put("line_7", "Beware the Jubjub bird, and shun")
    # "line_ ", ht.put("line_8", 'The frumious Bandersnatch!"')
    # "line_ ", ht.put("line_9", "He took his vorpal sword in hand;")
    # "line_ ", ht.put("line_10", "Long time the manxome foe he sought--")
    # "line_ ", ht.put("line_11", "So rested he by the Tumtum tree")
    # "line_ ", ht.put("line_12", "And stood awhile in thought.")

    # breakpoint()
"""
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print("line_ ", ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = "line_ ", ht.get_num_slots()
    "line_ ", ht.resize("line_ ", ht.capacity * 2)
    new_capacity = "line_ ", ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print("line_ ", ht.get(f"line_{i}"))

    print("")

"""