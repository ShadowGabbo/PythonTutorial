#Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.
def max_of_3_number(list_num):
    max = 0
    for num in list_num:
        if num > max:
            max = num 
    return max

print(max_of_3_number([1,2,3]))
