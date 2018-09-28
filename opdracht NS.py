def standaarttarief(afstandKM):
    if afstandKM < 1:
        afstandKM = 0
        prijs = 0
    elif afstandKM > 0 and afstandKM < 50:
        prijs = afstandKM * 0.80
    elif afstandKM > 50:
        prijs = afstandKM * 0.60 + 15
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaarttarief(afstandKM)
    if leeftijd < 12 or leeftijd > 64 and weekendrit == 'nee':
        eindtarief = prijs * 0.70
    elif leeftijd < 12 or leeftijd > 64 and weekendrit == 'ja':
        eindtarief = prijs * 0.65
    elif weekendrit == 'ja':
        eindtarief = prijs * 0.60
    else:
        eindtarief = prijs
    print('Je reist ', afstandKM, 'KM en betaald een prijs van €', eindtarief)

ritprijs(int(input('Wat is je leeftijd:? ')), input('Ga je reizen in het weekend:? '), int(input('Hoeveel kilometer ga je reizen:? ')))