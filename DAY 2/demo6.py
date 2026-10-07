# # #demo4.py 

# # name='abhi'
# # age=23
# # sal=3300.00
# # company='cisco'
# # print(f'Employee name is:{name}')
# # print(f'Employee age is:{age}')
# # print(f'Employee salary is:{sal}')
# # print(f'Employee company is:{company}')

# # print(f'''Employee name is:{name}
# # age is:{age}
# # salary is:{sal}
# # company is:{company}''')

# # name='ram'
# # age=24
# # salr=33000.00
# # company='cisco'

# # print(name, age, salr, company)
# # v=salr*0.18
# # print('employees tax is:',v)
# # total=salr+v
# # print(total)

# # appname=int(input('enter the port number:'))
# # if appname == 5000:
# #     print('Flask is running')
# # else:
# #     print('not runnning ')

# # app_name = input('Enter app name: ')

# # if app_name in 'crm application running in flask web app':
# #     port = 5000
# # else:
# #     port = 8080
    
# # print(f"App Name is:{app_name} Running Port Number is:{port}")

# appname=input('enter the name:')
# if appname in 'flask is 5000':
#     print('flask is running')
# elif appname in 'fastapi in 8080':
#     print('fastapi is running')
# elif appname in 'pormethus in 9090':
#     print('pormethus is running')
# else:
#     print('default appname is',appname,'and pnumber is 8000')


# appname=input('enter the name:')

# if appname == 'flask':
#     port = 5000
# elif appname == 'fastapi':
#     port = 8080
# elif appname == 'pormethus':
#     port = 9090
# else:
#     appname = 'web 2.0'
#     port = 8000

# print('appname is', appname, 'and port is', port)

# pin=1234
# count = 0
# while count < 3:
#     userpin = int(input('enter a pin:'))
#     if pin == userpin:
#         print('pin is correct')
#         break
#     count+=1

# else:
#     print('not correct')

# l1=[]
# print(len(l1))
# count = 0
# while count < 5:
#     hostname=input('enter the hostname:')
#     l1.append(hostname)
#     count = count+1

# print(len(l1))

# for x in l1:
#     print(x)


# read=input('enter the hostname to read:')

# if read in l1:
#     print('is in the list')
# else:
#     print('not in the list')


# l1[4]=10
# print(l1)

# total=0
# for x in l1:
#     total=total+int(x)
# print(total)

# for x in read:
#     print(x)

hosts = [] # empty list
print(f"Number of elements in the list:{len(hosts)}") # display number of elements in the list

c = 0
while c < 5:
    h = input("Enter a hostname:")
    hosts.append(h) # append the hostname to the list
    c = c + 1

print(f"\nNumber of elements in the list:{len(hosts)}") # display number of elements in the list

for var in hosts:
    print(var) # iterate through the list and display each hostname
    

host_name  = input("Enter a hostname:")
if host_name in hosts:
    hosts[-1] = host_name 
else:
    hosts.append(host_name) # add the hostname to the list

print("\n") # empty line
for var in hosts:
    print(var) # display the list of hostnames