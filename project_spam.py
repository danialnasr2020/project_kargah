import re

def is_spam(word):
   
    uppercase_count = sum(1 for c in word if c.isupper())
    if uppercase_count > 2:
        return True

    word_lower = word.lower()

    
    for char in word_lower:
        if word_lower.count(char) >= 3:
            return True

    
    vowels = "aeiou"
    if not any(v in word_lower for v in vowels):
        return True

    
    if not re.fullmatch(r"[a-zA-Z]+", word):
        return True

    return False


text = input("enter your text: ")


words = text.split()


for word in words:
    if is_spam(word):
        print(f"'{word}' → spam")

