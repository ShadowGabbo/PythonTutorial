#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
def char_counter_pro(lista_a):
    return [len(parola) for parola in lista_a]

print(char_counter_pro(["bella","tre","quattro"]))    