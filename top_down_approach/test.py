#Hash tables
"""
    The most typical way to memoize is by using hashtables. Hashtables are arrays that can be indexed
    using variables types other than integers. As we have already seen, we may need to store results against
    strings, floats, and even objects. Hashtables allow us to do all of this quite easily. The only condition 
    for using hashtables is that keys should unique. In python, we can use the dictionary data structures as a 
    hashtable. The dictionary allow us to store data in the form of key-value pairs in an unordered collection of
    data values.
"""

#playing around hashtable => flashback to object
dictionary = {}

key = 'name'
value = "AJibola"

dictionary[key] = value
dictionary['lastname'] = "Adebayo"
dictionary['age'] = 25
dictionary[1995] = 2022

class Dummy:
    def __init__(self, val) -> None:
        self.val = val
        pass
new_class = Dummy(22)
dictionary[new_class] = 10

for key, value in dictionary.items():
    print(key, value)
# print(dictionary)