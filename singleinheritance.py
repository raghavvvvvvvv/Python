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
                self.net = self.sal+self.hra+self.da+self.ta
            def print(self):
                print("employee number ",self.eno)
                print("employee name ", self.ena)
                print("basic salary ", self.sal)
                print("House Rent ", self.hra)
                print("Dearness allowance", self.da)
                print("Travelling Allowance ", self.ta)
                print("eNet Salary", self.net)
