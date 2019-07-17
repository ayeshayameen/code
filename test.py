print("hi")


def ayesha():
    print("nice girl")



ayesha()


class Emp:

    def __init__(self,eid,ename,eage,esal,eaddress='Pune'):
        self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empSalary = esal
        self.empAddress = eaddress

    def __str__(self):
        return '\n EmpId : {}, EmpName : {}, EmpAge : {}, EmpSalary : {}, EmpAddress : {}'.format(self.empId,self.empName,self.empAge,self.empSalary,self.empAddress)


    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.empId == other.empId

    def __hash__(self):
        return self.empId

e=Emp(1,'ayesha',25,500000)
print(e)


e2=Emp(2,'xyz',25,1000000000000)
print(e2)


e2=Emp(3,'qwe',28,1000000000000)
print(e2)

for row in range(1,6):
    for col in range(1,row+1):
        print("@",end="")
    print()


