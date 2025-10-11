import re

SPAM_WORDS_LIST = ["Python", "Guido van Rossum"]

def remove_spam(message: str) -> str:
    for spam_word in SPAM_WORDS_LIST:
        # Екрануємо спеціальні символи, які можуть бути в spam_word
        escaped_word = re.escape(spam_word)
        # Використовуємо \b лише на краях слів
        message = re.sub(rf"\b{escaped_word}\b", "*", message)
    return message

assert remove_spam("Guido van Rossum") == '*'
assert remove_spam("Python") == '*' # '******'
assert remove_spam("Guido van Rossum Python") == '* *'

print(remove_spam("Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0."))