#Building an Arcade Score Tracker

#Keep the code running until the user says stop
while True :
    score = input("Enter Your Score: ").strip().lower()

 #Check if the user wants to stop the game session
    if score == "stop" :
     print("Game Session Ended!")
     break
    
 #Convert the score into an integer
    score = int(score) 

    if score > 100:
      print ("Wow.!! New High Score")
    else :
      print("Good Try, Keep Playing!")