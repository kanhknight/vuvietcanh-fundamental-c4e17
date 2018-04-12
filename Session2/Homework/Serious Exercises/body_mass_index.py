# Body Mass Index
m = float(input("Please input your weight: "))
h = float(input("Please input your height(cm): "))
h = h/100
b = m/(h**2)
if b < 16:
    print("Severely underweight")
elif b >= 16 and b <18.5:
    print("Underweight")
elif b >= 18.5 and b < 25:
    print("Normal")
elif b >= 25 and b < 30:
    print("Overweight")
else:
    print("Obese")