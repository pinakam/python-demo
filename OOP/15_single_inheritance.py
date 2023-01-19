# Parent class
class Employee:
    company = "Moweb"

    def showDetails(self):
        print("This is an Employee")


# Base/Derived/Child Class of the Employee
class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")


e = Employee()  # Object of the Employee class
e.showDetails()  # Call from the Employee class method using its own object
p = Programmer()  # Object of the Employee class
p.getLanguage()  # Call from the Programmer class method using its own object
print("Company Name ===>>> ", p.company)  # Access parent class variable using child class object
