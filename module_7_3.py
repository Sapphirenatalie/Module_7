from random import randint, uniform

team1 = 'Мастера кода'
team2 = 'Волшебники данных'

team1_num = randint(5, 15)
team2_num = randint(1, 15)

score_1 = randint(40, 80)
score_2 = randint(40, 80)
tasks_total = score_1 + score_2

team1_time = round(uniform(5000,  10000), 5)
team2_time = round(uniform(5000,  10000), 5)

time_avg = round((team1_time + team2_time)/tasks_total, 2)

# Использование %:
print("В команде %s участников %12d!" % (team1, team1_num))
print("В команде %s участников %7d!" % (team2, team2_num))
print("Итого сегодня в командах участников: %5s и %s!" % (team1_num, team2_num))

# Использование format():
print("Команда {} решила задач: {:11}!".format(team1, score_1))
print("Команда {} решила задач: {:6}!".format(team2, score_2))

print("{} решили задачи за {} с!".format(team1, team1_time))
print("{} решили задачи за {} с!".format(team2, team2_time))

# Использование f-строк:
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f"Победа команды {team1}!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f"Победа команды {team2}!"
else:
    result = f"Ничья!"

challenge_result = result

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
