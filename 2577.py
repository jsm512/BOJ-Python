number=int(input())*int(input())*int(input())
number=str(number)
for i in range(10):
    print(number.count(f'{i}'))