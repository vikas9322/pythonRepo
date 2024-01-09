print("Welcome to treasure island your misssion is to find the treasure")
left = "left"
right = "right"
print(f"please make your choise {left} or {right} \n")
direction = input().lower()

if(direction == left):
    choise1 = "swim"
    choise2= "wait"
    print(f"please make your choise {choise1} or {choise2} \n")
    final_choise = input().lower()
    
    if(final_choise == choise2):
        door1 = "red" , "blue" , "yellow"
        door2 = "blue"
        door3 = "yellow"
        print(f"please make your choise {door1}, {door2} or {door3} \n")
        doorChoise = input().lower()
        
        if(doorChoise == door2):
            print("game Over")
        elif(doorChoise==door1):
            print("game Over")
        else:
            print("conratulations!!!! you win")
    else:
        print("game over")
else:
    print("game over")
