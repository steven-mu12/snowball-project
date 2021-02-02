##########################################
# AGGRESSIVEAL - A SNOWBALL FIGHTING BOT   
# DESIGNED BY HARIS VEKAR AND STEVEN MU  
# CODED BY STEVEN MU    
# TESTED AND CAREFULLY CHECKED BY MOHAMED AYED
##########################################

#Strategy: Being agressive (key to winning the game) while keeping an eye on other key variables in order to stay in the game longer. Kind of like HalTheHoarder and PatientPam Combined, but a lot lot more smart and is able to make very accurate reads.

def getMove(myScore, mySnowballs, myDucksUsed, myMovesSoFar, opponentsScore, opponentsSnowballs,opponentsDucksUsed, opponentMovesSoFar):
  
  # Defining some variables used. Full_Throw here is the boolean that initiates the "full-auto-machinegun" feature of this bot.
  full_throw = False
  diff1 = int(1) 
  diff2 = int(2)

  # The Bot algorithm
  while myScore or opponentsScore < 3:

   # Reloading twice to start
    if myMovesSoFar == []:
      return "RELOAD"
    
    elif myMovesSoFar == ["RELOAD"]:
      return "RELOAD"

    # We made use of the variable "mySnowballs" as a general varaible to set up more checks. This way, we can control snowBall cheating very easily.

    #########
    # If we have 0 snowballs, we can only duck or reload;
    #########

    if full_throw == True:
      full_throw = False

    if mySnowballs == 0:

      # if we only have 1 life left, we would check a few other conditions (like opponentsScore or opponentsSnowballs, plus a lot more) to make a decision. This multiple-nested-if-statements check style continues throughout this program, so pasting this message over and over again would make this program look a little messy. 

      if opponentsScore == 2:

        if opponentMovesSoFar[-1] == "RELOAD":
          if opponentsSnowballs > 0 and myDucksUsed < 5:
            return "DUCK"
          else:
            return "RELOAD"

        else:
          if myDucksUsed < 5:
            return "DUCK"
          else:
            return "RELOAD"

      # if we have 2 lives left
      elif opponentsScore == 1:

        if opponentMovesSoFar[-1] == "RELOAD":
          if opponentsSnowballs > 1 and myDucksUsed < 5:
            return "DUCK"
          else:
            return "RELOAD"

        else:
          return "RELOAD"

      # if we have all 3 lives left:
      else:
        if opponentMovesSoFar[-1] == "RELOAD":
          if opponentsSnowballs > 2 and myDucksUsed < 5:
            return "DUCK"
          else:
            return "RELOAD"

        else:
          return "RELOAD"

    #########
    # If we have between 1 and 3 snowballs: 
    #########

    elif mySnowballs >= 1 and mySnowballs <= 3:
      # if we only have 1 life left

      if full_throw == True:
        return "THROW"
        if mySnowballs == 1:
          return "RELOAD"
        else:
          return "THROW"

      elif opponentsScore == 2:
        if opponentsSnowballs == 0:
          return "RELOAD"

        elif opponentsSnowballs in [1, 2, 3, 4, 5]:

          if myScore == 2:
            return "THROW"

          elif myScore == 1:
            if myDucksUsed < 5 and opponentsSnowballs > 0:
              return "DUCK"
            else:
              return "THROW"

          else:
            if myDucksUsed < 5 and opponentsSnowballs > 0:
              return "DUCK"
            else:
              return "THROW"

        elif opponentsSnowballs in [6, 7, 8, 9, 10]:
          if myScore == 2:
            return "THROW"

          else:
            return "RELOAD"

      # if we have 2 or 3 lives left
      elif opponentsScore in [0, 1]:
        
        if opponentsSnowballs == 0:
          return "THROW"
          full_throw = True

        elif opponentsSnowballs in [1, 2]:
          if myScore == 2:
            return "THROW"

          elif myScore == 1:
            if mySnowballs > opponentsSnowballs:
              return "THROW"
            else:
              return "THROW"

          else:
            return "RELOAD"
        
        elif opponentsSnowballs in [3, 4, 5]:
          if myScore == 2:
            return "THROW"

          elif myScore == 1:
            if mySnowballs == opponentsSnowballs or opponentMovesSoFar[-1] == "RELOAD":
              return "THROW"
            else:
              if myDucksUsed < 5:
                return "DUCK"
              else:
                return "RELOAD"
          
          else:
            if diff1 > 0 and myDucksUsed < 5:
              return "DUCK"
              diff1 = opponentsSnowballs - mySnowballs
            else:
              return "THROW"
              full_throw = True
          
        elif opponentsSnowballs in [6, 7, 8, 9, 10]:
          if myScore in [1, 2]:
            return "THROW"
          elif opponentMovesSoFar[-1] == "RELOAD":
            return "RELOAD"
          else:
            if myDucksUsed < 5:
              return "DUCK"
            else:
              return "THROW"
            
    #######        
    # If we have between 4 and 7 snowballs
    #######

    elif mySnowballs >= 4 and mySnowballs <= 7:

    # if we only have one life left:
      if full_throw == True:
        return "THROW"
      
      elif opponentsScore == 2:
        if opponentsSnowballs == 0:
          return "RELOAD"
        
        elif opponentsSnowballs in [1,2,3,4,5]:
          if myScore == 2:
            return "THROW"
            full_throw = True
          elif myScore == 1:
            if opponentMovesSoFar[-1] == "RELOAD":
              return "THROW"
              full_throw = True
            else:
              return "RELOAD"

          else:
            if opponentMovesSoFar[-1] == "RELOAD":
              return "THROW"
              full_throw = True
            else:
              return "THROW"  # THIS USED TO BE "RELOAD" IF IT WAS THROW IN THE FIRST PLACE IT WOULDVE WON US THE SEMI FINALS

        elif opponentsSnowballs in [6,7,8,9,10]:
          if myScore == 2:
            return "THROW"
            full_throw = True
          elif myScore in [0,1]:
            if diff2 > 0 and myDucksUsed < 5:
              return "DUCK"
              diff2 = opponentsSnowballs - mySnowballs
            else:
              return "THROW"
              full_throw = True

    # If we have 2 or 3 lives left
      else:
        if opponentsSnowballs == 0:
          return "THROW"
          full_throw = True
        
        elif opponentsSnowballs in [1,2,3,4]:
          if myScore == 2:
            return "THROW"
            full_throw = True
          else:
            if opponentsScore + 1:
              return "THROW"
              full_throw = True
            else: 
              return "THROW"
              full_throw = True

        elif opponentsSnowballs in [5,6,7,8,9]:
          if myScore == 2:
            if myDucksUsed < 5:
              return "DUCK"
            else:
              return "THROW"
              full_throw = True
          
          else:
            return "RELOAD"
        
        else:
          if myScore == 2:
            return "DUCK"
          else:
            if opponentsSnowballs > 7:
              return "DUCK"
            elif opponentsScore + 1:
              return "RELOAD"
            else:
              return "THROW"
              full_throw = True

    ########
    # If we have 8 to 10 Snowballs, we would check the condition mySnowballs to see if it's below 10 before reloading. Else, we would machine gun.
    ########
    
    elif mySnowballs in [8,9,10]:
      if opponentsSnowballs >= 8 and myDucksUsed < 5:
        return "DUCK"

      elif opponentsScore < 2:
        if mySnowballs < 10:
          return "RELOAD"
        else:
          return "THROW"
          full_throw = True

      else:
        return "THROW"
        full_throw = True

  
