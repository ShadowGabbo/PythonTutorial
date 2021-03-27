#Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

def istogramma(lista):
    for numero in lista:
        print("*" * numero)

print(istogramma([1,2,3]))