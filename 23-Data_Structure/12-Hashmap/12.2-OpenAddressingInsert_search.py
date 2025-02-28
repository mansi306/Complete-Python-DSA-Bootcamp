class Hashmaps:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.slots = [None]* self.capacity
        self.values = [None] * self.capacity 
    
    def hash_function(self,key):
        return abs(hash(key)) % self.capacity
    
    def rehash(self,old_hash_value):
        return (old_hash_value+1) % self.capacity
    
    def insert(self,key,value):
        hash_value = self.hash_function(key)
        initial_index = hash_value
        if self.slots == None:
            self.slots[hash_value] = key 
            self.values[hash_value] = value
        else:
            # update if key is already present 
            if (self.slots[hash_value]==key):
                self.values[hash_value] = value
                return 
            else:
                new_hash_value = self.rehash(hash_value)
                # continue probing until empty slot is found or key is found 
                while self.slots[new_hash_value]!=None and self.slots[new_hash_value]!=key:
                    new_hash_value = self.rehash(new_hash_value)
                if (self.slots[new_hash_value]== None):
                    self.slots[new_hash_value]= key 
                    self.values[new_hash_value]= value
                else:
                    # key  already present 
                    self.values[new_hash_value]= value

    def get(self,key):
        initial_index = self.hash_function(key)
        
        current_position = initial_index
        while self.slots[current_position] != None:
            if (self.slots[current_position]==key):
                return self.values[current_position]
            current_position = self.rehash(current_position)
            if (current_position==initial_index):
                return "Not found "
        return "Not found !"
    
    def delete(self,key):
        initial_index = self.hash_function(key)
        current_position = initial_index
        while self.slots[current_position]!=None:
            if (self.slots[current_position]==key):
                self.slots[current_position]=None
                self.values[current_position] = None
                print(f"{key} has been deleted")
                return 
            current_position = self.rehash(current_position)
            if (current_position==initial_index):
                break 
        print(f'{key} not found ')

    def __setitem__(self,key,value):
        return self.insert(key,value)
        
    def __getitem__(self,key):
        return self.get(key)
    
    def __str__(self):
        result = []
        for i in range(self.capacity):
            if (self.slots[i]!=None):
                result.append(f"{self.slots[i]}:{self.values[i]}")
        return '\n'.join(result)
            
# m1 = Hashmaps(3)
# m1.insert("apple",10)
# m1.insert("chiku",11)
# m1.insert("banana",12)
# print(m1.get('chiku'))
# m1.delete('chiku')
# print(m1.get("chiku"))
h1 = Hashmaps(3)
h1.insert("Apple",10)
h1['orange'] = 45
print(h1)
print(h1.get("Apple"))
h1.delete("Apple")
print(h1.get("Apple"))
print(h1)