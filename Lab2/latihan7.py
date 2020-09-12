# meminta input dari user
print("Permainan 1 \nAndi vs Budi: ")
game1 = input().lower()
print("Permainan 2 \nAndi vs Cakra: ")
game2 = input().lower()
print("Permainan 3 \nBudi vs Cakra: ")
game3 = input().lower()


if game1 == "andi menang":
    if game2 == "andi menang":
        if game3 == "seri":
            print("Andi bermain batu")
            print("Budi bermain gunting")
            print("Cakra bermain gunting")
        else:
            print("tidak mungkin")
    elif game2 == "seri":
        value_cakra = "batu"
        if game3 == "cakra menang":
            print("Andi bermain batu")
            print("Budi bermain gunting")
            print("Cakra bermain batu")
    else:
        print("tidak mungkin")

elif game1 == "budi menang":
    if game2 == "seri":
        if game3 == "cakra menang":
            print("Andi bermain gunting")
            print("Budi bermain batu")
            print("Cakra bermain gunting")
        else:
            print("tidak mungkin")
    elif game2 == "cakra menang":
        if game3 == "seri":
                print("Andi bermain gunting")
                print("Budi bermain batu")
                print("Cakra bermain batu")
    else:
        print("tidak mungkin")

elif game1 == "seri":
    if game2 == "seri":
        if game3 == "seri":
            print("Andi bermain batu")
            print("Budi bermain batu")
            print("Cakra bermain batu")
        else:
            print("tidak mungkin")
    else:
        print("tidak mungkin")

else:
    print("tidak mungkin")
    
        
