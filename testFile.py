from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("Jul %d, %Y %H:%M:%S PM")
print("date and time =", dt_string)
#Jul 23, 2022 8:12:29 PM