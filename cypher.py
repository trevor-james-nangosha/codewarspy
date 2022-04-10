"""You have been asked to write a simple cypher algorithm that rotates a character by 13 chars
    and numbers by 5 chars and returns a new cyphered string.
    NOTES:
    The letters are in the range[a-z,A-Z] and the numbers are in the range[0-9]
    Any special characters are ignored by the algorithm.
"""

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

def cipher(word):
    newWord = ""
    newNumber = ""
    for char in word:
        if char == " ":
            newWord += char
            continue
        elif char not in letters and char not in numbers:
            continue        
        elif char in letters:
            newChar = rotateLetter(char)
            newWord += newChar    
            continue    
        elif char in numbers:
            newNumber = rotateNumber(char)
            newWord += newNumber
            
    return newWord    

def rotateLetter(letter):
    """Rotates the letter by 13 characters and returns the new character."""
    newPosition = letters.index(letter) + 13
    if newPosition > len(letters) - 1:
        newPosition = newPosition%13
        newChar = letters[newPosition]
    newChar = letters[newPosition]
    return newChar

def rotateNumber(number):
    """Rotates the number by 5 characters and returns the number at the new position."""
    newPosition = numbers.index(number) + 5
    if newPosition > len(numbers) - 1:
        newPosition = newPosition%5
        newNumber = numbers[newPosition]
    newNumber = numbers[newPosition]
    return newNumber

def decipher(cipheredString):
    """Deciphers the string ciphered by our cipher algorithm."""
    pass

password = cipher("bachelor of science in software engineering year 2 semester 1")
originalString = decipher(password)