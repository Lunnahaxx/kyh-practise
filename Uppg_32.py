"Uppg_Skriv ett Pythonprogram som tar in en sträng från användaren, och skriver ut följande:"


"Task info"
"""
32.1 Längden på strängen
32.2 Om strängen är ett "palindrom" eller ej. Exempel på palindrom: rattar, Ebbe. 
Observera att programmet ska klara att användaren blandar stora och små bokstäver!
32.3 Utöka programmet så att även uttryck som "Aja Baja" anses vara palindrom, d.v.s 
filtrera bort alla mellanslag ifrån inputsträngen!

Tips: använd det vi lärde oss igår kring att vända en sträng och/eller lista baklänges, 
och join-funktionen. Även list comprehension kan komma till användning. "
"""
"-------------------------"
"Koden Uppg_ "
"Lösningen"
strang = input("Skriv en sträng så får du längden: ")
strang_lenght = len(strang)
strang_backwards = ''.join(list(reversed(strang)))

print("Hemlig info: ", strang, strang_backwards)

if strang.lower() == strang_backwards.lower():
    print("Det är ett palindrom. ")
else:
    print("Ej ett palindrom. ")




"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"
