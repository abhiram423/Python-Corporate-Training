# import time

# obj=open('pin_log','a')
# pin=1234
# count=0
# while(count<3):
#     p = input("Enter PIN: ")
#     count=count+1
#     if (int(p) == pin):
#         print('pin correct', count)
#         obj.write(f'PIN correct {count}\n')
#         break
#     else:
#         obj.write(f'failed {p}\n')

# if (int(p)!=pin):
#     print('PIN incorrect')
#     obj.write(f'PIN incorrect {p}\n')
# obj.close()


# from os import read
# import pprint

# dic={}
# file=open("network.cfg","r")
# data=file.read()
# print(data)
# data=data.split(',')
# dic['eid']=103
# print(dic)
# pprint.pprint(dic)


# file=open('demo1.py','r')
# data=file.read()
# print(data)
# file.close()

# file=open('demo2.py','r')
# data=file.readline()
# data=file.readline()
# print(data)
# file.close()

file=open("demo1.py",'w')
file.write("Abhiram Vedantham ")
file.close()


