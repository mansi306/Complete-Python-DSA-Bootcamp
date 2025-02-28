hashmap = {}
hashmap['one']= 1
print(hashmap)


def count_frequency(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1 
        else:
            hashmap[num] = 1 
    return hashmap

print(count_frequency([1,2,3,4,1,2,1,2,3,4,5,3,2,1]))



def group_anagrams(words):
    anagram = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram:
            anagram[sorted_word].append(word)
        else:
            anagram[sorted_word] = [word]
    return list(anagram.values())


words = ['eat','tea','tan','ate','nat','bat']
print(group_anagrams(words))
