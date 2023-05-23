
#https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single
import os
import jokehandler

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nFörläng livet med dåligt skämt")

    url= f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

    nr = 1
    jokeobject = jokehandler.Jokehandler(url)

    while True:

        t_joke = jokeobject.get_joke()

        print(f"\n{nr}.---------------------------")
        print(f"{t_joke}")
        print("---------------------------\n")

        nr += 1

        entill =  input("Vill du ha en till? j/n")

        if (entill == "n" or entill == "N"):
            break
main()