#d = {'c' : 5}

#['6']

#man loopar över nycklarna i dict
#for key in d:
    #print(f"{key} = {d[key]}")

"""18.1 Förklara vad nedanstående program gör för varandra!

people = {
“Fredrik”: “0702778511”,
“Olof”: “123456789”,
“Lisa”: “9999999999”,
“Bodil”: “555-666-789”
}

vem = input(‘Vem vill du ringa?’)
if vem not in people:
  print(‘Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog’)
else:
  number = people[vem]
  print(f”Numret till {vem} är {number}”)

18.2 Modifiera programmet så antalet personer i telefonkatalogen skrivs ut när man kör programmet
18.3 Flytta in all kod i en "main"-funktion som anropas på slutet av programmet. Main ska varken ta argument, eller returnera något
18.4 Ge användaren ett val mellan "Slå upp" och "Lägg till/skriv över" nummer."""




#print(people)

def main():
    people = {
        'Fredrik': '0702778511',
        'Olof': '123456789',
        'Lisa': '9999999999',
        'Bodil': '555-666-789'
    }
    print(f"Antal i listan: {len(people)}")
    vem = input("Vem vill du ringa?")
    if vem not in people:
        print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
    else:
        number = people[vem]
        print(f"Numret till {vem} är {number}")


if __name__ == '__main__':
    main()
