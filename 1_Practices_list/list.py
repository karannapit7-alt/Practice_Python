#Basic operation with lists 
str = "Hello"
list = list(str) 
print(list)

list =['a','b','c','d','e']
print('a' in list )
print('x' in list)

#Sorted list 
list = [1,4,9,10,9,3,5,12]
list1 = sorted(list)
print(list1)

#set list 
list = [1,2,1,2,8,9,5,9,8,2,10]
list1 = set(list)
print(list1)

#Methods of list 
#Append list
list = [1,2,85,96,78,236,78,45,20,30,78,20]
list.append(230)
print(list) 

#insert list
list = [1,2,85,96,78,236,78,45,20,30,78,20,230]
list.insert(4,7)
print(list)

#Count list 
list = [1,5,2,3,1,5,2,7,9]
list1 = list.count(1)
print(list1)

#index list 
list = [1,5,4,3,6,7,8,9,10]
list1 = list.index(6)
print(list1)

#POP list 
list = [1,2,3,4,5,6,7,8,9,10]
list.pop(5)
print(list)

#Remove list
list = [1,2,3,4,5,6,7,8]
list.remove(4)
print(list)
