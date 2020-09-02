
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
        return (self.length/self.capacity)

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
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # if self.length == 0: # THIS MIGHT NOT BE NEEDED!

        # if key == 'line_7':
        #     breakpoint()
        hash_value = self.fnv1(key)
        print('key, value, hash value, length, capacity',key, value, hash_value, self.length, self.capacity)
        current_entry = self.list[hash_value]
        # IF COMMON HASH VALUE
        if current_entry is not None:
            # add to linked list / tail is head (more efficient)
            # LOOP THROUGH LINKED LIST IN CURRENT ENTRY
            while current_entry:
                print('okkayyy....')
                if current_entry.key == key: # COMMON HASH VALUE AND SAME KEY
                    current_entry.value = value #UPDATE VALUE EXISTING KEY
                elif current_entry.next:
                    current_entry = current_entry.next
                else: #NEW NODE IN ELEMENT
                    print('then...')
                    if self.get_load_factor() > .7:
                        print('capacity, rehashing')
                        self.resize(2*self.capacity)
                    hash_value = self.fnv1(key) #**** RISKY
                    ll = HashTableEntry(key,value)
                    # breakpoint()
                    ll.next = self.list[hash_value]
                    self.list[hash_value] = ll # TODO test
                    self.length += 1
                break

        # NO COMMON HASH VALUE        
        else:
            if self.get_load_factor() > .7:
                self.resize(2*self.capacity)    
            hash_value = self.fnv1(key) #***RISKY
            ll = HashTableEntry(key, value)
            self.list[hash_value] = ll # this will be the head
            self.length += 1
    



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        try:
            hash_val = self.fnv1(key)
            entry = self.list[hash_val]
            val = entry.value
            # print(key == entry.key)
            while entry:
                # if key == 'line_12':
                #     breakpoint()
                # MATCH IS ON THE NEXT KEY AND TWO MORE NODES TILL LEAF (e.g. root --> match --> leaf)
                if entry.next is not None and entry.next.next is not None and entry.next.key == key:
                    # print('*1')
                    entry.next = entry.next.next
                    self.length -= 1
                    entry = entry.next

                # MATCH ON THE ROOT NODE AND THERE IS AT LEAST ONE MORE NODE (e.g. match --> next -->.....)
                elif self.list[hash_val].key == key and entry.next is not None: #and entry.next.next 
                    # print('*1-root node')
                    new_head = entry.next #***
                    self.list[hash_val] = new_head #entry.next
                    self.length -= 1
                    entry = None #Nasty code!!
                    # breakpoint()

                # next node is the last node and matches key    
                elif entry.next is not None and entry.next.key == key and entry.next.next is None: #third condition is redundant but just in case
                    # print('*2')
                    # breakpoint()
                    entry.next = None
                    self.length -= 1
                    entry = entry.next
                
                # next node is the last node and the current node key matches key -> NEED TO TEST
                elif entry.next is not None and entry.key == key:
                    # print('*3')
                    # breakpoint()
                    entry = entry.next
                    self.length -= 1

                    entry = entry.next

                else: # only one node exists
                    # print('*4')
                    self.list[hash_val] = None
                    self.length -= 1
                    entry = None


            
                # elif entry.key == key and entry.next:
                #     self.list[hash_val] = entry.next
                #     entry = entry.next
                # elif entry.key == key:
                #     self.list[hash_val] = None
                    

            print(f"removed {key}: {val}")
            # breakpoint()

            # if self.get_load_factor() < .2:
            #     self.resize(self.capacity/2)
            # print(self.size, self.capacity, self.list)

        except ValueError:
            print('No match found')
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        value = None
        # breakpoint()
        try:
            
            entry = self.list[self.fnv1(key)]
            while entry:
                if entry.key == key:
                    value = entry.value
                    entry = entry.next
                else:
                    entry = entry.next
        except ValueError:
            value = None
        return value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        #self: list, capacity, length
        old_list = self.list
        new_list = [None]*new_capacity
        self.list = new_list # test
        self.length = 0 #reset length
        self.capacity = new_capacity # test
        for i in range(len(old_list)): # loop through old list
            current_entry = old_list[i]
            if current_entry:
                while current_entry:
                    self.put(current_entry.key, current_entry.value)
                    current_entry = current_entry.next
                
        # print('new list post', self.list, 'k', k, 'j',j)
        

        # breakpoint() # to test new_hash


        
if __name__ == "__main__":
    ht = HashTable(8)

    "line_ ", ht.put("line_1", "A")# 
    "line_ ", ht.put("line_2", "B")#
    "line_ ", ht.put("line_3", "C")#
    "line_ ", ht.put("line_4", "D")
    "line_ ", ht.put("line_5", "E"),
    "line_ ", ht.put("line_6", "F")
    "line_ ", ht.put("line_7", "G")

    # for i,val in enumerate(ht.list):
    #     if val:
    #         while val: 
    #             print(i, val.key, val.value, ht.fnv1(val.key))
    #             val = val.next
    
    "line_ ", ht.put("line_8", "H")
    "line_ ", ht.put("line_9", "I")
    "line_ ", ht.put("line_10", "J")
    "line_ ", ht.put("line_11", "K")
    "line_ ", ht.put("line_12", "L")
    # print(ht.list)
    # print(ht.list, ht.length, ht.capacity)
    # print()
    # print(ht.get("line_4"))
    # print(ht.get("line_5"))
    # print(ht.get("line_14"))
    # TODO build your own helper display functions
    for i,val in enumerate(ht.list):
        if val:
            while val: 
                print(i, val.key, val.value, ht.fnv1(val.key))
                val = val.next
    
    # print('length', ht.length, 'capacity', ht.capacity)
    # print(len(ht.list))

    print(ht.delete('line_8')) #line_8 - 'H'

    for i,val in enumerate(ht.list):
        if val:
            while val: 
                print(i, val.key, val.value, ht.fnv1(val.key))
                val = val.next
    print(ht.delete('line_3')) #line_3 - 'C'

    for i,val in enumerate(ht.list):
        if val:
            while val: 
                print(i, val.key, val.value, ht.fnv1(val.key))
                val = val.next
    print(ht.delete('line_10')) #line_10 - 'J'

    for i,val in enumerate(ht.list):
        if val:
            while val: 
                print(i, val.key, val.value, ht.fnv1(val.key))
                val = val.next
    print(ht.delete('line_12')) #line_12 - 'L'

    for i,val in enumerate(ht.list):
        if val:
            while val: 
                print(i, val.key, val.value, ht.fnv1(val.key))
                val = val.next
    breakpoint()

    # print(ht.get('line_9'))
    # print(ht.get('line_12'))
    print(ht.get('line_7'))
    # print(ht.list)
    # breakpoint()

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