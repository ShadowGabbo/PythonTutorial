#Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi, e che ti dica in output se l'elemento passato sia presente o meno nella lista.
#Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.

def search(word, list_words):
    if word in list_words:
        return True
    return False

print(search("ciao",["porco","per"]))