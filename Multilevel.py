class Employee:
    def input_data(self):
        self.eno =input("input employee number ")
        self.ena =input("input employee name ")
        self.sal = input("input basic salary ")
        class Salary(Employee):
            def calc(self):
                self.hra=self.sal*40/100
                self.da=self.sal*30/100
                self.ta = self.sal*20/100
                self.gross = self.sal+self.hra+self.da+self.ta
        class NetSalary(Salary):
            def calc(selfself):
                self.pf=self.sal*12/100
                self.it=self.sal*10/100
                self.pt=self.sal*8/100
                self.ded=self.pf+self.it+self.pt
            def print(self):
                print("employee number ",self.eno)
                print("employee name ", self.ena)
                print("basic salary ", self.sal)
                print("House Rent ", self.hra)
                print("Dearness allowance", self.da)
                print("Travelling Allowance ", self.ta)
                print("Net Salary", self.gross)
                print("Providient Fund", self.pf)
                print("Providient Fund", self.pf)
                print("Providient Fund", self.pf)
                print("Net Salary", self.net)
