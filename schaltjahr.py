# Programm zur Berechnung, 
# ob ein bestimmtes Jahr ein Schaltjahr ist

# Gibt True falls Schaltjahr
def ist_schaltjahr( jahr ):
    if( jahr % 2 == 0 ):
        return True
    return False

jahr = eval( input("Bitte gib eine Jahreszahl ein: ") )
print( "Schaltjahr" if ist_schaltjahr(jahr) else "Kein Schaltjahr" )
