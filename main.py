primer = input('Введите пример: ').replace(' ', '')
result = ''
if '+' in primer:
    primer2 = primer.replace('+', '')
    if primer2.isdigit():
        primer2 = primer.split('+')
        result = int(primer2[0])+int(primer2[1])
    else:
        result = 'В примере есть ошибка'
elif '-' in primer:
    primer2 = primer.replace('-', '')
    if primer2.isdigit():
        primer2 = primer.split('-')
        result = int(primer2[0])-int(primer2[1])
    else:
        result = 'В примере есть ошибка'
elif '*' in primer:
    primer2 = primer.replace('*', '')
    if primer2.isdigit():
        primer2 = primer.split('*')
        result = int(primer2[0])*int(primer2[1])
    else:
        result = 'В примере есть ошибка'
elif '/' in primer:
    primer2 = primer.replace('/', '')

    if primer2.isdigit():
        primer2 = primer.split('/')
        if int(primer2[1]) == 0:
            result = 'На ноль делить нельзя'
        else:
            result = int(primer2[0])/int(primer2[1])
    else:
        result = 'В примере есть ошибка'

print(result)
