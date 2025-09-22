n = int(input("Enter the target value: "))
m = int(input("Enter the maximum value in range: "))
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        if i + j == n:
            print("Found!")
            print(f"First number = {i} and Second number = {j}")
            break
    else:
        continue
    break
else:
    print("No pair found that adds up to the target value.")
