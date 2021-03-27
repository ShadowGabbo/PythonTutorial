#In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
#Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".
#Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.

def language(string):
    new=""
    vowels = ["a","e","i","o","u"]
    for char in string:
        if not char in vowels:
            new+=char+"o"+char
        else:
            new+=char
    return new

print(language("mangiare"))
