def removeVowels(s: str):
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            s = s.replace(char, "")
    return s


print(removeVowels("hello"))
