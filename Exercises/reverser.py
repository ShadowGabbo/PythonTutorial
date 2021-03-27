#Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")
def reverser(string):
    return string[::-1]

print(reverser("hey"))