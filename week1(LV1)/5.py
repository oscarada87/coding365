a = float(input())
b = float(input())
n = int(input())
temp1 = a + b
temp2 = a - b
temp3 = a * b
print(a)
print('%.{}f'.format(n) % temp1)
print('%.{}f'.format(n) % temp2)
print('%.{}f'.format(n) % temp3)
