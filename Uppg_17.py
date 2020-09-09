"""Bygg ett program där användaren ser denna meny:

1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet

Programmet ska spara en fil "TODO.txt" som läses in i början, och innehåller en
 lista med saker att göra.
Listan kan manipuleras med alternativ 2 och 3.

När programmet avslutas sparas listan till TODO.txt (skrivs över).

Detta är ett miniprojekt! Jag rekommenderar att ni fortsätter jobba
tillsammans utanför lektionstid för att bli klara.
Diskutera hur ni ska lösa uppgiften först tillsammans."""

from pathlib import Path
p = Path("todo.txt")
content = p.read_text()
lines = content.splitlines()

#todo_lista = []


print("Detta är en todo-lista, välj ett val: ")
print("1 - Öppna TODO listan")
print("2 - Lägg till uppgift")
print("3 - Ta bort uppgift")
print("4 - Avbryt programmet")

todo_list = []
todo_list.append(p.read_text())

def user_input():
    answer = input("Gör ditt val: ")

    while True:

        if answer == "1":
                    print(p.read_text())
        if answer == "2":
            p.read_text()#läser upp vad som finns i listan
            user_input2 = input("Lägg till uppgift:")
            todo_list.append(user_input2)
            p.write_text(f"{todo_list}")


            #CL p.write_text(input("Lägg till uppgift:"))
        #if answer == "3":

        if answer == "4":
            quit()
        user_input()


if __name__ == '__main__':
        user_input()