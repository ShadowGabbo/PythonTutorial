#Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri
def mul_list(list_num):
    mul = 1
    for num in list_num:
        mul*=num
    return mul

print(mul_list([1,2,3,4]))