# # L1=[1,2,'hi',12.0, True]
# # print(L1)
# # print(type(L1))
# # for item in L1:
# #     print(item, type(item))
# # L1.append('new_item')
# # print(L1)
# # L1.insert(3, 6)
# # print(L1)


# # l1=[]
# # print(len(l1))

# # limit=5
# # while len(l1)<limit:
# #     h=input('enter a hostname:')
# #     l1.append(h)
# #     # limit+=1
    
# # print(len(l1))

# # for x in l1:
# #     print(x)


# # string

# s='hello ,world,programm ,python'
# s.split(',')
# print(s)

# print(','.join(s))

# total=0
# Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']
# for x in Emp:
#     eid,ename,edept,ecost=x.split(',')
#     print(ename.title(),edept.upper())
#     total=total+int(ecost)
    
# print(total)


# l=[('1','2'),('3','4')]
# l.append(5)
# print(l) 

# t=([1,2],[3,4])
# print(t)
# print(len(t))
# t[1].append(5)



# dicts={'key1':'value1','key2':'value2'}
# for var,val in dicts.items():
#     print(var,val)


# l1={}
# print(len(l1))
# count = 0
# while len(l1) < 5:
#     host = input('enter a name:')
#     ip = input('enter a ip')
#     l1[host]=ip
# print(len(l1))

# for var in l1:
#     print(l1[var])


import pprint


emp={}


emp['eid']=[101,102,103,104]
emp['ename']=['john','ram','raju','bibu']
emp['edept']=['sales','prod','hr','sales']  
emp['dob']={'DOB':[{'DOB':'1st Jan'},{'DOB':'2nd Jan'},{'DOB':'3rd Jan'},{'DOB':'4th Jan'}]}


#print(emp)  
pprint.pprint(emp)


    