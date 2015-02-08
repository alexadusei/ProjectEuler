#-------------------------------------------------------------------------------
# Name:        Name Scores

# Purpose:     Using 'q022.txt', a 46K text file containing over five-thousand
#              first names, begin by sorting it into alphabetical order. Then
#              working out the alphabetical value for each name, multiply this
#              by its alphabetical position in the list to obtain a name score.
#              For example, when the list is sorted into alphabetical order,
#              COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
#              name in the list. So, COLIN would obtain a score of
#              938 x 53 = 49714. What is the total of all name scores in the
#              file?
#
# Answer:      871198282

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

# Helper function to read names, strip quotation marks and sort all names
def readNames():
    file = open("q022.txt")
    names = []

    for line in file:
        temp = []
        temp = line.split(",")
        for name in temp:
            names += [name.strip("\"")]

    names.sort()
    return names

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
names = readNames()
sum = 0

for i in range(len(names)):
    wordSum = 0
    for k in range(len(names[i])):
        wordSum += ALPHABET.index(names[i][k]) + 1

    sum += wordSum * (names.index(names[i]) + 1)

print sum