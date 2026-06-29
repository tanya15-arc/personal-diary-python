print("♡" * 30)
print( "☆"*5, " MY PERSONAL DIARY",  "☆" *5)
print( " Today's Entries" )
print("♡"*30)

while True:
    print("\n========= MENU==============")
    print("  choose one option from 1-4")
    print( "1. Adding thoughts 📚 ")
    print(" 2. Read diary♡")
    print(" 3. Delete diary ■")
    print(" 4. Exit 》》")

    choice=int(input(" Enter your choice : "))
    
    if(choice == 1):
        diary = input(" Write today's diary: ")
        with open("diary.txt" , "a") as file:
            file.write(diary + "\n")
        print("《 Entry saved successfully 》")
        
        
        
    elif( choice == 2):
        try:
            with open("diary.txt", "r") as file:
                content = file.read()
                if ( content== " "):
                    print( " Diary is empty ;)")
                else:
                    print("\n----------- MY DIARY-------------")
                    print(content)
        except FileNotFoundError :
            print(" No diary found yet")
        
        
    elif( choice == 3):
        with open("diary.txt" , "w") as file:
            pass
        print(" 《 Diary cleared successfully 》")
        
        
    elif(choice == 4):
        print(" Bye babu ! see yah !")
        break
        
    else:
        print(" Invalid choice ! Please enter 1-4")


