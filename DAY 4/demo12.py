class Enrollment:
    name = ''
    dob = ''
    place = ''
    def initialize(self,n,d,p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'Emp {self.name} enrollment is done')
    def display(self):
        print(f'About {self.name} detials:-')
        print(f'Name:{self.name} DOB:{self.dob} Place:{self.place}')
        
obj1 = Enrollment()
obj1.initialize('Arun','1st Jan','City-1')

obj2 = Enrollment()
obj2.initialize('Leo','2nd Feb','City-2')

obj1.display()
obj2.display()

obj3 = Enrollment()
obj3.display()


class Enrollment:
    def __init__(self,n,d,p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'Emp {self.name} enrollment is done')
    def display(self):
        print(f'About {self.name} detials:-')
        print(f'Name:{self.name} DOB:{self.dob} Place:{self.place}')
        
obj1 = Enrollment('Arun','1st Jan','City-1')

obj2 = Enrollment('Leo','2nd Feb','City-2')

obj1.display()
obj2.display()


import time
class vendor:
    def __init__(self,vName,vGST):
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} enrollment is done')
    def billing(self,pName,pQty=0,pCost=0.0):
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost
        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.total + self.tax
        s1=f'{self.vName}\t{self.vGST}\t{self.pName}\t{self.pQty}'
        s2=f'\t{self.pCost}\t{self.total}\t{self.gs}'
        s3=f'\t{time.ctime()}\n\n'
        with open('vendor_prods.log','a') as wobj:
            wobj.write(s1+s2+s3)


vobj1 = vendor('Klabs','GST1234')
vobj2 = vendor('Xserver','GST5593')
vobj1.billing('pA',5,1250)
time.sleep(2)
vobj2.billing('pB',2,435.2)
time.sleep(5)
vobj1.billing('pB',4,250)


'''This is Vendor-Product billing app'''
import time
class vendor:
    '''this is vendor class - initialize vendor details'''
    def __init__(self,vName,vGST):
        '''initialize vendor details'''
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} enrollment is done')
    def billing(self,pName,pQty=0,pCost=0.0):
        '''this is non-constructor billing method do product billing and update to log file'''
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost
        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.total + self.tax
        s1=f'{self.vName}\t{self.vGST}\t{self.pName}\t{self.pQty}'
        s2=f'\t{self.pCost}\t{self.total}\t{self.gs}'
        s3=f'\t{time.ctime()}\n\n'
        with open('vendor_prods.log','a') as wobj:
            wobj.write(s1+s2+s3)




"""Demonstrates weak aggregation between a department and a teacher.

In this example, the `Dept` class stores a reference to a `Teacher` object,
but it does not create or own that teacher. The teacher is created outside
of the department and then passed in. This is a loose association, which is
known as weak aggregation.
"""


class Teacher:
    """Represents a teacher that can exist independently.

    The teacher object is not controlled by any department. It can be used in
    different places without being tightly coupled to one container.
    """

    def __init__(self, name):
        self.name = name

    def teach(self):
        """Print a teaching message for the teacher."""
        print(self.name, "is teaching")


class Dept:
    """Represents a department that aggregates a teacher reference.

    This is weak aggregation because the department simply keeps a reference to
    a `Teacher` object and does not own its lifecycle. The teacher may still
    exist even if the department is removed or changed.
    """

    def __init__(self, teacher):
        self.teacher = teacher


# Teacher is created independently outside the department.
teacher1 = Teacher('Ram')

# Dept only holds a reference to the teacher; this is weak aggregation.
dept = Dept(teacher1)

# The department uses the teacher object without owning it.
dept.teacher.teach()