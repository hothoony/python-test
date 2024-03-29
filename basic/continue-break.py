
print()
print('-------------- 1')
for i in range(1, 11, 1):
    print(i)

print()
print('-------------- 2')
for i in range(1, 11, 1):
    print(i)
    if i == 5:
        break

print()
print('-------------- 2')
for i in range(1, 11, 1):
    if i % 2 != 0:
        continue
    print(i)
