#Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
def sum_list(list_num):
    sum = 0
    for num in list_num:
        sum+=num
    return sum

print(sum_list([1,2,3,4]))