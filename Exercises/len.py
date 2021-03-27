#Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!

def len_str(str):
    len = 0
    for char in str:
        len+=1
    return len

print(len_str("Ciao"))