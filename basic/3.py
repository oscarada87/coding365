import math

def main():
    num1 = float(input())
    num2 = float(input())
    Sum = num1 + num2
    Difference = abs(num1 - num2)
    Product = num1 * num2
    Quotient = num1 / num2
    temp = '%.3f'% Quotient
    temp = str(temp)
    # print(temp)
    print('Sum:%.2f' % Sum)
    print('Difference:%.2f' % Difference)
    print('Product:%.2f' % Product)
    print('Quotient:{}'.format(temp[:-1]))

main()
