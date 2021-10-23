i = 0
numbers = []
print(f"At the top i is {i}.")

def addI(max):
    for i in range(0, max):
        print(f"For now, i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print("Ending this loop, i is ", i)

addI(12)
print("The numbers: ")

for num in numbers:
    print(num)