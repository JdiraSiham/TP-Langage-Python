#Realisée par : JDIRA Siham

import string

def frequence_des_mots(texte):
    d = {}
    for mot in texte.split():
        mot = mot.strip(string.punctuation).lower()
        if mot:
            d[mot] = d.get(mot, 0) + 1
    return d

def longueur_moyenne_des_mots(texte):
    mots = [mot.strip(string.punctuation) for mot in texte.split() if mot]
    longueurs = [len(mot) for mot in mots]
    return sum(longueurs)/len(longueurs) if longueurs else 0

def mots_plus_et_moins_utilises(texte):
    freq = frequence_des_mots(texte)
    plus = []
    moins = []
    max_occ = 1
    min_occ = None
    for valeur in freq.values():
        if valeur > max_occ:
            max_occ = valeur
        if min_occ is None or valeur < min_occ:
            min_occ = valeur
    for mot, valeur in freq.items():
        if valeur == max_occ:
            plus.append(mot)
        if valeur == min_occ:
            moins.append(mot)
    return plus, moins

def detection_des_palindromes(texte):
    mots = [mot.strip(string.punctuation).lower() for mot in texte.split()]
    palindromes = [mot for mot in mots if len(mot) > 1 and mot == mot[::-1]]
    return palindromes

def nombre_de_phrases(texte):
    phrases = [p.strip() for p in texte.replace("!", ".").replace("?", ".").split(".") if p.strip()]
    return len(phrases), phrases

def longueur_des_phrases(phrases):
    longueurs = [len(p.split()) for p in phrases]
    moy = sum(longueurs)/len(longueurs) if longueurs else 0
    return longueurs, moy

def types_de_ponctuation_utilises(texte):
    ponctuation_trouvee = set([ponc for ponc in texte if ponc in string.punctuation])
    return ponctuation_trouvee

def top_10_des_mots(texte):
    freq = frequence_des_mots(texte)
    top = []
    for i in range(10):
        max_mot = max(freq, key=freq.get)
        top.append((max_mot, freq[max_mot]))
        del freq[max_mot]
    return top

def phrase_la_plus_longue(phrases):
    max_phrase = phrases[0]
    max_len = len(max_phrase.split())
    for p in phrases:
        if len(p.split()) > max_len:
            max_len = len(p.split())
            max_phrase = p
    return max_phrase

def patterns_repetitifs(texte):
    freq = frequence_des_mots(texte)
    return [mot for mot, nb in freq.items() if nb > 1]

with open("texte.txt", "rt") as f:
    texte = f.read()

print(f"Fréquence des mots : {frequence_des_mots(texte)}")
print(f"Longueur moyenne des mots : {longueur_moyenne_des_mots(texte):.2f}")
plus, moins = mots_plus_et_moins_utilises(texte)
print(f"Mots les plus utilisés : {plus}")
print(f"Mots les moins utilisés : {moins}")
print(f"Palindromes : {detection_des_palindromes(texte)}")
nb_phrases, phrases = nombre_de_phrases(texte)
print(f"Nombre de phrases : {nb_phrases}")
longueurs_phrases, moy_phrases = longueur_des_phrases(phrases)
print(f"Longueur moyenne des phrases : {moy_phrases:.2f}")
print(f"Top 10 des mots : {top_10_des_mots(texte)}")
print(f"Phrase la plus longue : {phrase_la_plus_longue(phrases)}")
print(f"Ponctuation utilisée : {types_de_ponctuation_utilises(texte)}")
print(f"Patterns répétitifs : {patterns_repetitifs(texte)}")