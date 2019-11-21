"""Q1"""
mylist = ['Apple', 1, 1.2222, 10, 20]
for x in mylist :
    print(x)




"""Q2"""
ourlist=[10,20,30,50,60,40,80]
print(sum(ourlist))



"""Q3"""
myllist = [10,20,30,44,27]
print(max(myllist))





"""Q4"""
a = [10,20,30,20,10,50,60,40,80,50,40]
b=list(set(a))
a=b
print(a)






"""Q5"""
e = []
if(len(e)== 0 ):
    print("list is empty")
else:
    print("list is not empty")






"""Q6"""
a = (10,20,{"a","d","e","r"},60,40,80)
for x in a:
    print(x)





"""Q7"""
num_set= set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print(x)



"""Q8

s1={1,2,3,4,5,6}
s2={2,4,6} 
print ( s1 & s2 )

"""












"""Q9

setx = set(["green","blue"])
sety = set(["blue","yellow"])
seta = setx | sety
print(seta)


-Solution


{'yellow', 'blue', 'green'}

"""






"""Q10
seta =set([5,10,3,15,2,20])
print(len(seta))

Solution
6
"""








"""Q11

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)    


"""










"""Q12

a = "Hello , World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))

-Solution
e
llo
orl
14
hello , world!
Jello , World!

"""


