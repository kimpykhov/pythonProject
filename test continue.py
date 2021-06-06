while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины') # Разные другие действия здесь...


a, b = int(input()), str(input())
for i in range(len(b)):
    print(chr(ord(b[i]) + a), end='')