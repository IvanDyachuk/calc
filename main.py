primer = input('Введите пример').replace(' ', '')
primer2 = ''
action = ''
if '+' in primer:
    action = '+'
    primer2 = primer.replace('+', '')
    if primer2.isdigit():
        primer2 = primer.split('+')
        Num1 = primer2[0]
        Num2 = primer2[1]
        print(int(Num1)+int(Num2))
    else:
        print('В примере есть ошибка')
elif '-' in primer:
    action = '-'
    primer2 = primer.replace('-', '')
    if primer2.isdigit():
        primer2 = primer.split('-')
        Num1 = primer2[0]
        Num2 = primer2[1]
        print(int(Num1)-int(Num2))
    else:
        print('В примере есть ошибка')
elif '*' in primer:
    action = '*'
    primer2 = primer.replace('*', '')
    if primer2.isdigit():
        primer2 = primer.split('*')
        Num1 = primer2[0]
        Num2 = primer2[1]
        print(int(Num1)*int(Num2))
    else:
        print('В примере есть ошибка')
elif '/' in primer:
    action = '/'
    primer2 = primer.replace('/', '')

    if primer2.isdigit():
        primer2 = primer.split('/')
        Num1 = primer2[0]
        Num2 = primer2[1]
        if int(Num2) == 0:
            print('На ноль делить нельзя')
        else:

            print(int(Num1)/int(Num2))
    else:
        print('В примере есть ошибка')
