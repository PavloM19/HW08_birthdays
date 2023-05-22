from collections import namedtuple
from datetime import datetime, timedelta


BD_User = namedtuple('BD_User', 'name birthday')
users = [BD_User('John', datetime(1980, 2, 29)), BD_User('Garry', datetime(1990, 5, 29)), BD_User('Fred', datetime(1986, 6, 2))]


def date_txt(date):
    return date.strftime('%d.%m')

def get_birthdays_per_week(users):
    today = datetime.today()
    today += timedelta(days=6-today.isoweekday())  #Start on saturday  
    nextweek_BD = [date_txt(today + timedelta(days=i)) for i in range(7)] #dates of BD's on next week

    dict_BD = {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : []}
    for user in users:
        user_data = date_txt(user.birthday)
        if user_data in nextweek_BD:
            num_day = nextweek_BD.index(user_data) - 2
            if num_day < 0:
                num_day = 0
            for i, k in enumerate(dict_BD):
                if i == num_day:
                    dict_BD[k].append(user.name)
                    break
    for k, v in dict_BD.items():
        if v:
            print(k, ': ' + ', '.join(v))


get_birthdays_per_week(users)

'''
1. получить текущую дату
2. найти даты (день и месяц) следующей недели + сб и вс текущей
3. найти юзеров у которых день и месяц рождения попадает 
4. вывести список именинников: 
Monday: Bill, Jill (сюда добавить всех у кого др был на выходных)
Friday: Kim, Jan

'''

