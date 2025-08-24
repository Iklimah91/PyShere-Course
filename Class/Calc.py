class maths_calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    def subtraction(self):
        return self.x - self.y
    def multiplication(self):
        return self.x * self.y
    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Error! Division by zero."
        
maths_calc.__call__ = maths_calc
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calc = maths_calc(num1, num2)
print(f"Addition: {calc.addition()}")
print(f"Subtraction: {calc.subtraction()}")
print(f"Multiplication: {calc.multiplication()}")
print(f"Division: {calc.division()}")
    
