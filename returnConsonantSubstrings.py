# given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant subStrings
# for example the word zodiacs, we cross out the vowels
# and we remain with
# z, d and cs
# so the answer is 26

letters = "abcdefghijklmnopqrstuvwxyz"
letterDict = {}

#populating the letterDict
startValue = 1
for letter in letters:
    letterDict[letter] = startValue
    startValue += 1

vowels = "aeiou"

def solve(string):
    subString = ""
    subStringArray = []
    for letter in string:
        if letter not in vowels:
            subString = subString + letter
        if letter in vowels and not subString == "":
            subStringArray.append(subString)
            subString = ""
        if letter == string[-1]:
            subStringArray.append(subString)

    result = 0
    resultsArray = []
    for subString in subStringArray:
        for letter in subString:
            value = letterDict[letter]
            result += value
        resultsArray.append(result)
        result = 0

    return max(resultsArray)


        





# pseudocode

# 1. start at the beginning

# look for consonant substrings
# a consonant substring is a group of consonants followed by a vowel
# keep an array of substrings

# start with an empty string
# and for each letter append to the empty string

# 2. traverse the string
# 3. for each letter in the word:
# 4.    if letter not vowel:
# 5.        append to the string
# 6.    if letter vowel:
#           add that particular substr to our array
# 7         reset our counter
# 6. at the end, go for all elements in our subString array
# 7. evaluate them 
# 8. return the highest

# nangosha = n, ng, sh