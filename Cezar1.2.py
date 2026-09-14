def alfabet_roman():
    litere = [
        'A','Ă','Â','B','C','D','E','F','G','H','I','Î','J','K','L','M','N','O','P','Q',
        'R','S','Ș','T','Ț','U','V','W','X','Y','Z'
    ]
    codificare = {litera: idx for idx, litera in enumerate(litere)}
    return litere, codificare

def cezar(text, k, operatie="c"):
    litere, codificare = alfabet_roman()
    rezultat = []
    text = text.replace(" ", "").upper()  # eliminarea spatiilor si transformarea in majuscule
    for ch in text:
        if ch not in codificare:
            print("Textul trebuie sa contina doar alfabetul roman")
            return None
        poz = codificare[ch]
        if operatie == "c":  # criptare
            noua_poz = (poz + k) % len(litere)
        elif operatie == "d":  # decriptare
            noua_poz = (poz - k) % len(litere)
        else:
            print("Alege 'c' sau 'd'.") 
            return None
        rezultat.append(litere[noua_poz])
    return "".join(rezultat)

def cezar_doua_chei(text, k1, k2, operatie="c"):
    if not (1 <= k1 <= 25): 
        print("Cheia 1 trebuie să fie între 1 și 25 inclusiv.")
        return None
    if not k2.isalpha(): #controlarea daca cheia 2 contine doar litere din alfabetul latin
        print("Cheia 2 trebuie sa contina doar litere ale alfabetului latin.")
        return None
    if len(k2) < 7:
        print("Cheia 2 trebuie să aiba lungimea de cel putin 7 caractere.")
        return None

    litere, codificare = alfabet_roman()
    rezultat = []
    text = text.replace(" ", "").upper()  # elimina spatiile si transforma in majuscule
    key2_shifts = [ord(c.lower()) - ord('a') for c in k2]

    for i, ch in enumerate(text):
        if ch not in codificare:
            print("Textul trebuie sa contina doar litere din alfabetul romanesc")
            return None
        poz = codificare[ch]
        shift1 = k1
        shift2 = key2_shifts[i % len(key2_shifts)]
        if operatie == "c":
            noua_poz = (poz + shift1 + shift2) % len(litere)
        elif operatie == "d":
            noua_poz = (poz - (shift1 + shift2)) % len(litere)
        else:
            print("Alege 'c' sau 'd'.")
            return None
        rezultat.append(litere[noua_poz])
    return "".join(rezultat)

# Alegerea tipului de criptare
msg = input("Introduce mesajul: ")
operatie = input("Alege operatia (c=criptare / d=decriptare): ").strip().lower()
tip = input("Cu o cheie sau doua? (1/2): ").strip()

if tip == "1":
    k = int(input("Introduce prima cheie (1-25): "))
    output = cezar(msg, k, operatie)
elif tip == "2":
    k1 = int(input("Introduce prima cheie (1-25): "))
    k2 = input("Introduce a doua cheie (minim 7 litere): ")
    output = cezar_doua_chei(msg, k1, k2, operatie)
else:
    output = "Tip invalid. Alege 1 sau 2."

print("Rezultatul:", output)
