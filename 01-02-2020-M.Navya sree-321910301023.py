#tuple creation using tuple word
t2=tuple((10,20,30,40,50))
print(t2)
print(type(t2))


#Create a tuple with different data types
tuplex = ("Navya", False, 3.2, 1)
print(tuplex)



#convert a tuple to a string:
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
tuple = ('g', 'i', 't', 'a', 'm') 
str = convertTuple(tuple) 
print(str) 


#slicing a tuple
t1=(1,2,3,4,"hello")
print(t1)
print(t1[1:4])


#length of the tuple
t1=(1,2,3,4,"hello")
print(len(t1))


#convert a tuple into dictionary
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

#reversing a tuple
t2=(1,2,3,4,"hello")
print(t2[::-1])


#list of tuples to dictionary
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
      
 
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),  
     ("suraj", 20), ("akhil", 25), ("ashish", 30)] 
dictionary = {} 
print (Convert(tups, dictionary))


#list to  a tuple
l1=[11,12,13,14,"ab","bc"]
t3=(l1)
print(t3)
