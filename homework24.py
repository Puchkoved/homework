import datetime


def check_password(pas):
    num = 0
    ST = 0
    st = 0
    s_c = 0
    space = 0
    other = ''
    special = ".,:;!_*-+()/#%&)"
    for i in pas:
        if i.isdigit():
            num += 1
        elif i.islower():
            st += 1
        elif i.isupper():
            ST += 1
        elif i in special:
            s_c += 1
        elif i ==' ':
            space += 1
        else:
            other += i
    if len(pas) < 8:
        raise Exception('Пароль слишком короткий')
    if num == 0:
        raise Exception('В пароле не хватает числа')
    if ST == 0:
        raise Exception('В пароле не хватает заглавной буквы')
    if st == 0:
        raise Exception('В пароле не хватает строчной буквы')
    if s_c == 0:
        raise Exception('В пароле не хватает спецального символа')
    if space != 0:
        raise Exception('В пароле не должно быть пробелов')
    if other != '':
        if len(other) > 1:
            s1 = 'е'
            s2 = 'ы'
        else:
            s1 = 'й'
            s2 = ''
        raise Exception(f'Недопустимы{s1} символ{s2} в пароле {other}')
    return print('Это хороший пароль!!!')


try:
    pas = input('Придумайте пароль\n'
                'Пароль должен состоять из 8 символов иметь строчные и заглавные буквы, а также цифры и спец символ\n'
                ': ')
    check_password(pas)
except Exception as exc:
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write('\n{txt: <65}'.format(txt=f'описание ошибки: {exc.args}'))
        f.write('{txt: <40}'.format(txt=f'   экземпляр ошибки: {pas}'))
        f.write(f'     время ошибки: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}')
