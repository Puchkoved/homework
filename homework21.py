class Team():
    teams = []

    def __init__(self, name, num, score, time, teams=teams):
        self.name = name
        self.num = num
        self.score = score
        self.time = time
        teams.append(self)

    def __lt__(self, other):
        if self.score > other.score:
            return self.name
        else:
            return other.name

    def middle_s(teams=teams):
        sum_s = 0
        for i in teams:
            sum_s += i.score
        return sum_s


    def middle_t(teams=teams):
        sum_t = 0
        for i in teams:
            sum_t += i.score*i.time
        return round(sum_t/Team.middle_s(),2)


team1 = Team('Мастера кода', 5, 40, 18015.2)
team2 = Team('Волшебники данных', 6, 42, 17157.3)

print('В команде Мастера кода участников: %s' % team1.num)
print('Итого сегодня в командах участников: %s и %s' % (team1.num, team2.num))
print('Команда Волшебники данных решила задач: {}'.format(team2.score))
print('Волшебники данных решили задачи за {}'.format(team1.time))
print(f'Команды решили {team1.score} и {team2.score} задач')
print(f'Результат битвы: победа команды {team1 > team2}')
tasks_total = Team.middle_s()
time_avg = Team.middle_t()
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
