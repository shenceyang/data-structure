

#define a list
x=[1,2,3]


#--------------------------------Add element to list-------------------------------
#append
x.append(4)

#extend: add a list to another list
x.extend([5,6,7]) #change x directly
print(x)

#insert: insert an element at the index
x.insert(0,100) 
print(x)
#---------------------------------------------------------------------------------------------




#-------------------------------delete element from list-------------------------------


#remove: remove the first element that matches the input
x=[1,2,3,2]
x.remove(2)
print(x)

#pop: remove the last element
x=[1,2,3,2]
x.pop()
print(x)

#pop: remove the element at the index
x=["a","b","c"]
x.pop(1)
print(x)

#clear:remove all
x=[1,2,3,2]
x.clear()
print(x)

#---------------------------------------------------------------------------------------------


#---------------------------------other list operation---------------------------------------

#reverse
x=[1,2,3]
x.reverse()
print(x)

#sort
x=[3,2,1]
x.sort()
print(x)
   

#copy
x=[1,2,3]
y=x.copy()

#zip
x=[1,2,3]
y=[4,5,6]
zipped = zip(x,y)
print(list(zipped)) #[(1, 4), (2, 5), (3, 6)]
#---------------------------------------------------------------------------------------------