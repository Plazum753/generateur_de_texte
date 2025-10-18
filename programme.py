from collections import Counter
from random import choice

with open("texte.txt",'r', encoding='utf-8') as f:
    texte = f.read()

texte = texte.lower().translate(str.maketrans('', '', '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~»«1234567890')).split()

dico = Counter()

for i in range(len(texte)-1):
    dico[(texte[i],texte[i+1])] += 1

def Un(phrase):
    mot = choice(list(dico.keys()))[0]
    maxi = 0
    for e in dico :
        if phrase[-1] == e[0] and maxi < dico[e]:
            mot = e[1]
            maxi = dico[e]
    return mot


dico2 = Counter()

for i in range(len(texte)-2):
    dico2[(texte[i],texte[i+1],texte[i+2])] += 1


def DEUx(phrase):
    mot = None
    maxi = 0
    for e in dico2:
        if phrase[-2] == e[0] and phrase[-1] == e[1] and maxi < dico2[e]:
            mot = e[2]
            maxi = dico2[e]
    return mot

def generateur(phrase):
    mot = DEUx(phrase)
    if mot == None:
        mot = Un(phrase)
    print(mot+" ", end="")
    phrase.append(mot)
    return phrase


phrase = input("Parle !\n")
phrase = phrase.lower().translate(str.maketrans('', '', '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~»«1234567890')).split()

for i in range(50):
    phrase = generateur(phrase)