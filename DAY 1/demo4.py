
# app_name = input('enter app name: ')

# if 'flask' in app_name.lower():
#     port = 5000
# else:
#     port = 8000

# print(f'The application "{app_name}" will run on port {port}.')


i=0
while (i < 5):
    print('test', i)
    i = i + 1


num=1234
count = 0
while count < 5:
    count +=1
    userpin=int(input('enter pin:'))

    if (userpin==num):
        print('correct pin')
        break
if (userpin!=num):
    print('incorrect pin')


val=[1,2,3,4]
total=0
for x in val:
    total = total+x
print(total)
print(val[::-1])

# Five common Python string methods:
# lower(), upper(), strip(), split(), replace()

