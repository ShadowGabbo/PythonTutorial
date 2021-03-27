#Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.
#Semplicemente, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}!

def char_freq(str):
    mappa = {}
    for carattere in str:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa

print(char_freq("ciao"))

 