digit = int(input(' Type seconds: ' ))
if 0 <= digit < 8640000:
    days,digit = divmod(digit, 24 * 60 * 60)
    hours,digit = divmod(digit, 60 * 60)
    minutes,sec = divmod(digit, 60)
    if 5 < days < 21:
        day_str = 'Днів'
    elif str(days)[-1] == '1':
        day_str = 'День'
    elif str (days)[-1] in ('234'):
        day_str = 'Дні'
    else:
        day_str = 'Днів'
    res = f'{days} {day_str}, {str(hours).zfill(2)}:{str(sec).zfill(2)}'
    print(res)
else:
    print('Bad data')


