"2.0.Uppg_ "
"Task info"
"""
Nu ska vi leka med att skicka parametrar till en databas!

OMDB är en IMDB-liknande hemsida på nätet, som också tillhandahåller
ett API där man kan göra sökningar.

26.1 Jag har fixat en API-nyckel åt oss! Därför kan vi använda detta
     webb-API (som är ett REST-API) och leka. Testa att skriva följande
     i en browser:

      http://www.omdbapi.com/?t=Alien&apikey=9f6d550c

     Ändra på "Alien" till en annan film!
26.2 Använd requests.get() med ovanstående URL, fast ta bort ? och framåt.
     Använd istället params={"t": "Alien", "apikey": "9f6d550c"} så kommer
     requests att lägga på ? och & och sånt strunt själv. :)

     Pretty printa (pprint) resultatet av ett i ett Pythonprogram!

26.3 Bygg ett Pythonprogram där användaren frågar efter en film, och skriv
     sedan ut en snygg infobox om filmen, typ så här:

*** Resultat från OMDB! ***
Alien (1979) regisserades av Ridley Scott.
      Skådisar: Tom Skerritt, Sigourney Weaver, Veronica Cartwright, Harry Dean Stanton
    IMDB betyg: 8.4
        Awards: Won 1 Oscar. Another 16 wins & 22 nominations.
         Längd: 117 min
"""
"-------------------------"
"Koden 2.0.Uppg_ "
"Lösningen"
import json
import requests
from pprint import pprint



#film = input("Sök här efter vilken film du vill ha info om: ")





def main():
    film = input("Sök efter vilken film du vill ha info om: ")
    r = requests.get("http://www.omdbapi.com/", params={f"t": film, "apikey": "9f6d550c"})
    # !list = r.json()
    text = r.text
    result = json.loads(text)
    pprint(result)

    year = result['Year']

    print("*** Resultat från OMDB! ***\n ")
    print(f"Title: {result['actors']}")
    print(f"Skådisar: {result['imdbRating']}")
    print(f"Skådisar: {result['actors']}")
    print(f"Skådisar: {result['actors']}")

if __name__ == '__main__':
    main()








#for i in result:
#    print(i["Title:"])


#pprint(list)

#for element in list:
 #   print(element['startDate'])

#Title
#Actors
#imdbRating



#for element in list:
    #print(element['startDate'])


#text = r.text
#list = json.loads(text)
#alternativt: \





"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"

"""
def main():
    pass



"""