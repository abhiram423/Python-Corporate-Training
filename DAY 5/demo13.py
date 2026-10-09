def display():
    '''display list of files'''
    for var in ['f1','f2','f3']:
        print(var)

class Cname:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    def display(self):
        '''display initialized values'''
        return self.a1,self.a2
#--------------------------------------------------
def connect(dsn):
    class Connection:
        def __init__(self,dsn,dbname,password):
            self.dsn = dsn
            self.dbname = dbname
            self.password = password
        def method1(self):
            return 'Query process'
    obj = Connection(dsn,'sqlite3','password')
    return obj



print("Welcome")
print("Test-1")
print("Test-2")
print("Test-3")
try:
    print(Test)
except Exception as eobj:
    print(eobj)
else:
    print("There is no Exception")
finally:
    print("Always running")
    
for var in range(5):
    print(var)
    print("-"*10)

total = 10 + 20
print("Total=",total)
print("End of the line")



import sys

try:
    fobj = open('invalidFile','r')
except PermissionError as eobj:
    print("This is 1st Except block")
    print(eobj)
except FileNotFoundError as eobj:
    print("This is 2n Exception block")
    print(eobj)

# Vs
try:
    fobj = open('InvalidFile','r')
except Exception as eobj:
    print(eobj)

print("") # empty line    
# Vs 
try:
    fobj = open('InvalidFile','r')
except Exception:
    print(sys.exc_info())