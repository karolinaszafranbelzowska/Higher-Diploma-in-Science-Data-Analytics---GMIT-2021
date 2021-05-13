# solution to problem number 7
# Karolina Szafran Belzowska, 2019/03/27
# An approximation of a square root ( Newton's method)
# Adapted from https://tour.golang.org/flowcontrol/8 and
# https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e (Dr Ian McLoughlin's video - week 8)

# The number to calculate the square root of 14.5
rootof = 14.5 
# The initial estimate for the square root
estimate = 1.0


while abs((estimate * estimate) - rootof) > 0.1:
    estimate -= (( estimate * estimate) - rootof) / (2 * estimate)

print(f"The square root of {rootof} is approx. {estimate}.")
