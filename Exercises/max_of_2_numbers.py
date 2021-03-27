#Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
#Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
def my_max(a, b):
    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("Il numero più grande tra i due è " + str(a))
    else:
        print("Il numero più grande tra i due è " + str(b))

print(my_max(3,5))


