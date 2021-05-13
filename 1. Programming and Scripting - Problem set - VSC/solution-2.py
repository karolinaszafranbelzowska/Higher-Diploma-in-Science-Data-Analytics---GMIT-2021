# Karolina Szafran Belzowska, 2019-03-15
# Is it a day that begins with letter T?
# Adapted from Dr Ian McLoughlin's video (Module Programming and scripting - week 1)

import datetime # This imports today's date and time.

if datetime.datetime.today().weekday() == 1 and 3: # datetime function to identify the current date and time
                                                   # Monday starts with 0, Tuesday with 1, and so on up until Sunday which is 6.
        
    print("Yes,today is a day which begins with a letter T")
else:
    # This states to the user not true if the above statements do not begin with the letter T.
    print("No, today is a day which does not begins with a letter T")
