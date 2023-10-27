
class Planet:
    " En klasse for å beskrive en planet"
    def __init__(self,navn:str,solavstand:float,radius:float, antallRinger=0) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius
        self.antallRinger = antallRinger

jorden = Planet( "Jorden", 152, 6371, 0)
mars = Planet("Mars", 227.9, 3389.5, 0)
jupiter = Planet("Jupiter", 778, 69911, 1)

# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen

print(jorden.radius)
print(mars.navn)
print(jupiter.antallRinger)

# OBS: pass på rekkefølgen i argumentene til konstruktøren.


