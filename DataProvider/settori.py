# Funzione di ricerca settore in base al numero inserito

def sector_find(numsect):
    global nomesettore
    if numsect == 1:
        nomesettore = "Basic Materials"
    elif numsect == 2:
        nomesettore = "Financial Services"
    elif numsect == 3:
        nomesettore = "Consumer Defensive"
    elif numsect == 4:
        nomesettore = "Utilities"
    elif numsect == 5:
        nomesettore = "Energy"
    elif numsect == 6:
        nomesettore = "Technology"
    elif numsect == 7:
        nomesettore = "Consumer Cyclical"
    elif numsect == 8:
        nomesettore = "Real Estate"
    elif numsect == 9:
        nomesettore = "HelthCare"
    elif numsect == 10:
        nomesettore = "Communication Services"
    elif numsect == 11:
        nomesettore = "Industrials"
    else:
        nomesettore = ""
        print("Numero non nel range previsto")
    return nomesettore
