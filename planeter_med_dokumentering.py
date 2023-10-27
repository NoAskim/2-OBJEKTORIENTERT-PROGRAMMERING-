
class Planet:
    """ En klasse for å lage planet-objekter 

    Parametre:
        navn (str): Planetens navn
        solavstand (float): Avstand fra sola i millioner km
        radius (float): Planetens radius i km
        antallRinger = 0 (int): Antall ringer rundt planeten
 """


    def __init__(self,navn:str,solavstand:float,radius:float, antallRinger=0) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius
        self.antallRinger = antallRinger

jorden = Planet( "Jorden", 152, 6371)

# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen

# OBS: pass på rekkefølgen i argumentene til konstruktøren.


