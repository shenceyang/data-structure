#define a string
s= "hello"


#count
count_h = s.count('h')

#find index
h_index = s.find('el')
h_index = s.index('el')
print(h_index)
#diff between find and index: find returns -1 if not found, index returns error if not found

#replace
x= s.replace('l','y')  #does not change the original string
print("x is {x}, s is {s}".format(x=x,s=s))

#split
s= "hello world"
s_list = s.split(' ')
print(s_list) #['hello', 'world']

#strip
s= " hello world "
s= s.strip()
print(s) #hello world

