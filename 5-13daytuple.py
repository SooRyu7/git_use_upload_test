day1 = ('monday' ,'tuesday','wednesday')
day2 = ('thursday','friday','saturday')
#('sunday')로 하면 튜플이 아니고 문자열
day3 = ('sunday',)

day = day1+day2+day3 #새로운 튜플.
print(type(day))
print(day)

day = day1 + day2 + day3 * 3
print(day)
