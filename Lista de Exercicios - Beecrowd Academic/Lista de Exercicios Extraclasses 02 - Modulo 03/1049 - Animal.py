animal_word_1 = input()
animal_word_2 = input()
animal_word_3 = input()

if animal_word_1 == 'vertebrado':
    if animal_word_2 == 'ave':
        if animal_word_3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if animal_word_3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if animal_word_2 == 'inseto':
        if animal_word_3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if animal_word_3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
