import random

def main():
    list = ["Ilana","Jonah","Moose","Bitch","Frenchie","Black Panther","Far","Dani","Fearless Leader","Etan","David","will Aaron show up?"]
    random.shuffle(list)
    j =0
    print("Team 1")
    for i in list:
        print(i)
        if j==5:
            print()
            print("Team 2")
        j+=1


if __name__ == "__main__":
        main()
