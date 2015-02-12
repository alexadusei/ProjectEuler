#-------------------------------------------------------------------------------
# Name:        Number Letter Counts

# Purpose:     If the numbers 1 to 5 are written out in words: one, two, three,
#              four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used
#              in total. If the numbers from 1 to 1000 (one thousand) inclusive
#              were written out in words, how many letters would be used?

#              NOTE: Do not count spaces or hyphens. For example, 342 (three
#              hundred and forty-two) contains 23 letters and 115 (one hundred
#              and fifteen) contains 20 letters. The use of "and" when writing
#              out numbers is in compliance with British usage.

# Answer:      21124

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine"]

# 'ten' is not a teen number, but kept here for the sake of simplicity
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]

tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
        "ninety"]

hundreds = "hundred"
thousands = "thousand"
conjunction = "and"
numbers = []
numSum = 0

for i in range(1, 1000+1):
    num = str(i)

    while len(num) != 0:

        if len(num) == 4:
            numbers += [digits[int(num[0])], thousands]
            num = num[3:]
        if len(num) == 3:
            if num[1] == '0' and num [2] == '0':
                numbers += [digits[int(num[0])], hundreds]
                num = num[2:]
            elif num[1] == '0':
                numbers += [digits[int(num[0])], hundreds, conjunction]
                num = num[1:]
            else:
                numbers += [digits[int(num[0])], hundreds, conjunction]
        elif len(num) == 2:
            if num[0] == '1':
                numbers += [teens[int(num[1])]]
                num = num[1:]
            else:
                numbers += [tens[int(num[0])-2]]
        else:
            numbers += [digits[int(num[0])]]

        num = num[1:]

print sum([len(numbers[i]) for i in range(len(numbers))])