naam = input("wat is je naam? ");
leeftijd = int(input("wat is je leeftijd? "))
gebruiker = naam + str(leeftijd)

if leeftijd <18:
    print(naam + ", je mag niet stemmen")

else:
    print( naam + ', je mag stemmen!')

