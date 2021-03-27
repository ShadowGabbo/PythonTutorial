#Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure meno.
def isPalindrome(string):
    return string==string[::-1]

print(isPalindrome("gok"))