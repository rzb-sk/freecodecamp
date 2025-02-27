def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    elif lang == 'ar':
        print('Salam')
    elif lang == 'en':
        print('Hello')
    else:
        print("Not recognized language, must be ALIEN!")

greet('es')
greet('fr')
greet('ar')
greet('en')
greet('kl')