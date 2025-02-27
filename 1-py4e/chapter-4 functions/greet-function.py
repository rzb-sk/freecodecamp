def greet(lang, name):
    if lang == 'en':
        return f'Hello {name.capitalize()}'
    elif lang == 'es':
        return f'Hola {name.capitalize()}'
    elif lang == 'fr':
        return f'Bonjour {name.capitalize()}'
    else:
        return f'We do not support this language. Must be ALIEN! {name.capitalize()}'

name = input("What's your name player! ")
lang = input("What's your preferred language? ")

print(greet(lang, name), ":)")