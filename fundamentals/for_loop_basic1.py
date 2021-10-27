# 1
for x in range(0, 151):
    print(x)
# 2
for x in range(5, 1001):
    if x % 5 == 0:
        print(x)
"""
for x in range(5, 1001, 5):
    print(x) 
test variation for #2
"""
# 3
for x in range(1, 101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
# 4
sum = 0
for x in range(0, 500000):
    if x % 2 == 1:
        sum = sum + x
print(sum)
# 5
for x in range(2018, 0, -4):
    print(x)
# 6
lowNum = 2
highNum = 10
mult = 3
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)
