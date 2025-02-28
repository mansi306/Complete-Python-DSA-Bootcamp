# from LinkedListForChaining import LLNode,LinkedList

# class Hashmaps:
#     def __init__(self,capacity):
#         self.capacity = capacity 
#         self.size = 0 
#         self.buckets = self.__create_buckets(self.capacity)

#     def __create_buckets(self, capacity):
#         buckets = []
#         for i in range(capacity):
#             buckets.append(LinkedList(i))
#         return buckets
    
#     def hash_function(self,key):
#         return (abs(hash(key)))% self.capacity
    
#     def rehash(self,key):
#         old_buckets = self.buckets
#         self.capacity = self.capacity*2
#         self.buckets = self.__create_buckets(self.capacity)
#         self.size = 0 
#         for eachHead in old_buckets:
#             current = eachHead.head 
#             while current!=None:
#                 self.insert(current.key,current.value)
#                 current = current.next



from collections import defaultdict
city_map = defaultdict(list)
city = ['mumbai','pune','kolkata']
city_map['India']+= city
print(city_map)

        