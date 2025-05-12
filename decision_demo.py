score = int(input("Enter your scope (0-100):"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

items = []
if items:
    print("There are items.")
else:
    print("The list is empty (Falsy).")