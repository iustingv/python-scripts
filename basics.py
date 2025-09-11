# 1. Variables
numbers = [10, 20, 30, "oops"]

def average(lst):
    total = 0
    count = 0
    for val in lst:
        try:
            total += float(val)
            count += 1
        except:
            print("Skipping:", val)
    return total / count if count else 0

with open("nums.txt", "w") as f:
    for n in numbers:
        f.write(str(n) + "\n")

vals = []
with open("nums.txt") as f:
    for line in f:
        vals.append(line.strip())

print("Values:", vals)
print("Average:", average(vals))

