var = 10 #escopooo global

def escopo():
    global var
    print(var)
    var = 7 #escopo local
    print(var)

escopo()

print(var)