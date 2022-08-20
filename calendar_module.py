# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

d = list(map(int, input().split()))
day_of_the_week = calendar.weekday(d[2], d[0], d[1])
day_conversion = dict({0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY",
                        4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"})
print(day_conversion[day_of_the_week])