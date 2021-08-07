#Part 12
from linked_list import Node, LinkedList
#Part 22
from blossom_lib import flower_definitions 


#Part 1
class HashMap:
  def __init__(self,size):
    self.array_size = size
    #Part 2, specifically:
    #Original code: self.array = [None for i in range(size)]

    #Part 13
    self.array = [LinkedList() for i in range(self.array_size)]

  #Part 3
  def hash(self,key):
    #Part 4
    hash_code = sum(key.encode())
    return hash_code

  #Part 5
  def compress(self,hash_code):
    return hash_code % self.array_size
  
  #Part 6/14
  def assign(self,key,value):
    array_index = self.compress(self.hash(key))
      #Part 14
    payload = Node([key,value])
    #Part 15
    list_at_array = self.array[array_index]
    #Part 16
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
    
    #Part 7
    #self.array[array_index] = [key,value]
    
    #Part 18
    list_at_array.insert(payload)

   #Part 8
  def retrieve(self,key):
    #Part 9
    array_index = self.compress(self.hash(key))
    #Part 19
    list_at_index = self.array[array_index]
    #Part 20
    for i in list_at_index:
    #Part 21
      if i[0] == key:
        return i[1]
    
    return None

    #Part 10
    payload = self.array[array_index]
    #Part 11
    if payload == None or payload[0] != key:
      return None
    if payload[0] == key:
      return payload[1]
    

#Part 23
blossom = HashMap(len(flower_definitions))

#Part 24
for element in flower_definitions:
  blossom.assign(element[0],element[1])

print(blossom.retrieve('wisteria'))


  

