class Employee:
    company = "Visa"
    eCode = 102


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Pinak"


p = Programmer()

print("Programmer Name: -> ", p.name)
print("Company Name ===>>> ", p.company)
print("Level is Before upgrade ==== >>>> ", p.level)
p.upgradeLevel()
print("Level is After upgrade ==== >>>> ", p.level)
