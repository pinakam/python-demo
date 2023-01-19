class Person:
    country = "India"
    state = "Gujarat"

    def getDetails(self):
        return {
            "country": self.country,
            "state": self.state
        }


class Employee(Person):
    company = "Moweb"
    salary = 100000

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def getDetails(self):
        print("Get details from the Employee class")


class Programmer(Employee):
    company = "Moweb Technologies"

    def getSalary(self):
        print("No salary to the programmer")


person = Person()
employee = Employee()
programmer = Programmer()

programmer.getDetails()
programmer.getSalary()
