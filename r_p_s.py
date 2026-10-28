import random


# stores the values
items = {
    1 :"rock",
    2 :"paper",             
    3 :"scisscor",
}

short_cut = ["rock","paper","scisscor"]

print("This is an 5 pointer game\nwho ever reaches 5 points first\nwins")

try :
    # value entering zone
    def enter():
        print("rock: 1\npaper: 2\nscisscor:3")
        out_put = random.choice(short_cut)
        value = int(input("enter a your chioce : "))
        in_put = items.get(value)
        return in_put , out_put   # used to return the value

    while True:
        # scoreboard initial
        comp_marks = 0     # marks list
        user_marks = 0
        # cause for reapting and crosscheacking the values and giving points

        while user_marks<5 and comp_marks<5:
            in_put ,out_put = enter()

            print(f"////YOU : {in_put}\t\t\tCOMPUTER :{out_put}////")

            if(in_put==out_put):
                print("\n\t\t\tIts a Tie")

            elif(in_put == "rock" and out_put == "paper"):
                print("\n\t\t\tComputer won a point")
                comp_marks+=1

                print("\n\t\t\t NEXT ROUND ")
                

            elif(in_put == "paper" and out_put == "scisscor"):
                print("\n\t\t\tComputer won a point")
                comp_marks+=1

                print("\n\t\t\t NEXT ROUND ")
                

            elif(in_put =="scisscor" and out_put == "rock"):
                print("\n\t\t\tComputer won a point")
                comp_marks+=1

                print("\n\t\t\t NEXT ROUND ")
                

            elif(in_put == "rock" and out_put == "scisscor"):
                print("\n\t\t\tYou have won ")
                user_marks+=1

                print("\n\t\t\t NEXT ROUND ")
                

            elif(in_put == "paper" and out_put == "rock"):
                print("\n\t\t\tYou have won ")
                user_marks+=1

                print("\n\t\t\t NEXT ROUND ")
                

            elif(in_put == "scisscor" and out_put == "paper"):
                print("\n\t\t\tYou have won ")
                user_marks+=1

                print("\n\t\t\t  NEXT ROUND ")

        #scoreboard final
        print(f"your score :{user_marks}    ||    computer score :{comp_marks}")

        # results
        if(user_marks == 5 ):
                print("\t\t\tHey You Have Won !!!")
        elif(comp_marks == 5):
                print("\t\t\tyou have lost")

        play_again = input("wanna play again (yes/no)  : ")
        if play_again!="yes": 
            print("Thanks for playing")
            break
        else:
            continue
except Exception as e:
     print(e)
        
            

