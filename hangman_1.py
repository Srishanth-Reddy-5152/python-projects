import random
set = {
    1: "ANIMALS",
    2: "FRUITS",
    3: "VEGETABLES",
    4: "ITEMS"
}

animl = ["girrafe","horse","dolfin","lion","tiger","zebra","elephant","monkey","gorrilla","bear","frog","pig","cat","hyna"]    
frt = ["apple","mango","melon","banana","grapes","kiwi","watermelon","dates","papaya","pineapple","gauva","muskmelon"]
veg = ["tomato","potato","spinach","carrot","okra","brocoli","cabbage","raddish","capsicum","brinjal","onion","beetroot"]
itms =["knife","ball","fridge","laptop","charger","phone","table","fan","dish","clothes","sofa","chair"]

chooser = int(input("ANIMALS = 1\nFRIUTS = 2 \nVEGETABLES = 3\nITEMS = 4\n enter the category number  :"))
def give_hint(inp,ran):
        hint = []
        for i in range(len(inp)):
            if(inp[i] == ran[i]):
                hint.append(inp[i])
            elif(inp[i] in ran):
                hint.append("*")
            else:
                hint.append("_")
        return "".join(hint)
attempts =5

if(chooser == 1):
    ran = random.choice(animl)
    print(f"HINT :  letters =   {len(ran)}")
    while attempts<6:
        inp = input("enter your guess  :")
        hint = give_hint(inp,ran)
        if(inp == ran ):
            print("CONGS U HAVE WON ")
            break
        else:
            print(f"HINT :{hint}")
            
elif(chooser == 2):
    ran = random.choice(frt)
    print(f"HINT : letters = {len(ran)}")
    while attempts<6:
        inp = input("enter your guess  :")
        hint = give_hint(inp,ran)
        if(inp == ran ):
            print("CONGS U HAVE WON ")
            break
        else:
            print(f"HINT :{hint}")
    
elif(chooser == 3):
    ran =random.choice(veg)
    print(f"HINT : letters =  {len(ran)}")
    while attempts<6:
        inp = input("enter your guess  :")
        hint = give_hint(inp,ran)
        if(inp == ran ):
            print("CONGS U HAVE WON ")
            break
        else:
            print(f"HINT :{hint}")
    

    
    
elif(chooser == 4):
    ran = random.choice(itms)
    print(f"HINT : letters = {len(ran)}")
    while attempts<6:
        inp = input("enter your guess  :")
        hint = give_hint(inp,ran)
        if(inp == ran ):
            print("CONGS U HAVE WON ")
            break
        else:
            print(f"HINT :{hint}")

    
else:
    print("<<<<<INPUT VALUE ENTERED>>>>>")  

# retry = print("wanna plya again").lowercase()
# if(retry="yes"):
    









