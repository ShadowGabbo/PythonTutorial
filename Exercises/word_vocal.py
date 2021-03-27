#Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.

def isaVocal(vocal):
    vocals = "aeiou"
    if vocal in vocals:
        print(f"{vocal} is a vocal")
    else:
        print(f"{vocal} isn't a vocal")

isaVocal("c")