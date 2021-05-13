# Karolina Szafran Belzowska, 2018-03-18
# Today is?
# This video helped me to solve the problem https://www.youtube.com/watch?v=HDe8InbWQJU,

import datetime
today = datetime.datetime.today()
f = "%A, %B %dth, %Y at %H:%M"
s = today.strftime(f)

print("Today is:", s)
