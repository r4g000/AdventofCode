# take input.txt and combine the first and last number and add these numbers together
with open("input.txt", "r") as f:
    data = f.read().splitlines()

values = []

for line in data:
    numbers = [digit for digit in line if digit in "0123456789"]
    values.append(int(numbers[0] + numbers[-1]))

print(sum(values))
