#Q.1- Get keys corresponding to a value in user defined dictionary
a=eval(input('enter dic'))
b=int(input("enter the value"))
flag=False
for i in a.items():
    
    if(b==i[1]):
        
        print(i[0])
#Q.2- Nested dictionary
d={}
for i in range(2):
    s=input("enter student name")
    for j in range(2):
        sub=input("enter subject ")
        marks=input("enter marks")
        d[s,sub]=[sub,marks]
name=input("enter name")
for j in d.items():
    for r in range(2):
        if(j[r][0]==name):
            print(j[1])
