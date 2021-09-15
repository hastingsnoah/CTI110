caffeine_mg = float(input())
''' Type your code here. '''
#do the math
hour6=caffeine_mg/2
format_hour6="{:.2f}".format(hour6)
hour12=hour6/2
format_hour12="{:.2f}".format(hour12)
hour24=hour12/2/2
format_hour24="{:.2f}".format(hour24)
#display after 6 hours
print("After 6 hours:",format_hour6,"mg")
#after 12 hours
print("After 12 hours:",format_hour12,"mg")
#after 24 hours
print("After 24 hours:",format_hour24,"mg")
