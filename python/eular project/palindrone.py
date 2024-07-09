values = []

for i in range(100, 1000):
    for j in range(100, 1000):
        value = str(i * j)
        if value[:3] == value[3:][::-1]:
            values.append(value)


values.sort()
for value in values:
    print(value)