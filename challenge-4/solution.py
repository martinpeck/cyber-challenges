count = 0

with open('test.txt', mode='r') as t:
    for line in t:
        for char in line:
            if char == "0":
                count += 1

print(count)
