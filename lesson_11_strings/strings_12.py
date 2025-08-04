# day = 13
# print("Сегодня пятница, {:10d}".format(day))
# print("Сегодня пятница, {:<10d}".format(day))
# print("Сегодня пятница, {:*<10d}".format(day))
# print("Сегодня пятница, {:*^10d}".format(day))
# print("Сегодня пятница, {:*>10d}".format(day))
#
# day = 13
# month = 10
# hour = 15
# print("Сегодня пятница: {1:10d}.{0:d}.{2:d}".format(month, day, hour))
#
# day = " пятница"
# month = "июнь"
# day_time = "morning "
# symbol = "*"
# print("Сегодня пятница: !{1:*>10}.{0}.{2:*<10}!".format(month, day, day_time))
# print("Сегодня пятница: !{1:*>10}.{0}.{2:*<10}!".format(month, day, day_time))
# print("Сегодня пятница: {3:*<5}{1: >10}.{0}.{2:*<10}!".format(month, day, day_time, symbol))

# print("Сегодня пятница, {day:10d}.{month}.{hour}!".format(month=10, day=13, hour=15))
# print("Сегодня пятница, {day:$>10}.{month}.{hour}!".format(month="июнь", day="пятница", hour="утро"))

day_time = 13
pi_num = 3.14159265

print("Сегодня пятница, {0:*>10.2f}!".format(day_time))
print("Число pi, {0:*>10.4f}!".format(pi_num))
