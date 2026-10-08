# l=[10,20,30,40,50]
# for x in l:
#     if x >30:
#         x=x+100
#         l.append(x)
#     else:
#         x=x+500
#         l.append(x)
# print(l)
# print(x)

print('hello workd')

n=[1,2,3,4,5]
even=[x*x for x in n ]
print(even)

n=['even' if x %2==0 else 'odd ' for x in range(1,6)]
print(n)

salaries=[20000,30000,40000,50000]
inc=map(lambda salaries:salaries+5000, salaries)
print(tuple(inc))

find=filter(lambda salaries: salaries>=40000, salaries)
print(list(find))

from functools import reduce
all=reduce(lambda x,y :x+y, salaries)
print(all)

total=0
for salary in salaries:
    total= total+salary
print(total)