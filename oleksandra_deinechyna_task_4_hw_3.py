Earth_days, Earth_hours = input('Пожалуйста, введите количество земных дней и часов через запятую: ').split(', ')
Mars_sol = round(1.02595675 * (int(Earth_days) + int(Earth_hours) / 24), 2)
print('{} Земных дней и {} часов равняются {} Марсианским солам'.format(Earth_days, Earth_hours, Mars_sol))
