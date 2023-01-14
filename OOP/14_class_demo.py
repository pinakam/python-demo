class CustomMath:
    @staticmethod
    def custom_addition(var1, var2):
        return var1 + int(var2)


customMath = CustomMath()
add = customMath.custom_addition(10, 20)
print("Addition of 2 nos is :-->> ", add)
