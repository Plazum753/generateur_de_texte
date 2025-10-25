from collections import Counter
from random import choice, choices

with open("texte.txt",'r', encoding='utf-8') as f:
    texte = f.read()

texte = texte.lower().translate(str.maketrans('', '', '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~»«1234567890')).split()

dico = Counter()

for i in range(len(texte)-1):
    dico[(texte[i],texte[i+1])] += 1

def Un(phrase):
    mots = []
    poids = []
    for e in dico :
        if phrase[-1] == e[0] :
            mots.append(e[1])
            poids.append(dico[e])
    if mots != []:
        return choices(mots,poids)[0]
    else :
        return choice(list(dico.keys()))[0]


dico2 = Counter()

for i in range(len(texte)-2):
    dico2[(texte[i],texte[i+1],texte[i+2])] += 1


def DEUx(phrase):
    if len(phrase)<2:
        return None
    mots = []
    poids = []
    for e in dico2:
        if phrase[-2] == e[0] and phrase[-1] == e[1] :
            mots.append(e[2])
            poids.append(dico2[e])
    if mots != []:
        return choices(mots,poids)[0]
    else :
        return None
    
dico3 = Counter()

for i in range(len(texte)-3):
    dico3[(texte[i],texte[i+1],texte[i+2],texte[i+3])] += 1


def TROIs(phrase):
    if len(phrase)<3:
        return None
    mots = []
    poids = []
    for e in dico3:
        if phrase[-3] == e[0] and phrase[-2] == e[1] and phrase[-1] == e[2] :
            mots.append(e[3])
            poids.append(dico3[e])
    if mots != []:
        return choices(mots,poids)[0]
    else :
        return None

def generateur(phrase):
    mot = TROIs(phrase)
    if mot == None:
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