# main.py

#imported stuff
import time
import random

#setting up variables
money = 100

cards = ["Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 
      7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

hand = []
dHand = []

#function to add cards to hand
def addToHand(pHand):
  card = random.randint(0,len(cards) - 1)
  pHand.append(cards[card])
  cards.remove(cards[card])
  
#function to return the sum of the cards in a hand
def handSum(pHand):
  sum = 0
  for i in range(len(pHand)):
    if pHand[i] == "J" or pHand[i] == "Q" or pHand[i] == "K":
      sum += 10
    elif pHand[i] == "Ace":
      pass
    else:
      sum += pHand[i]
  for i in pHand:
    if i == "Ace":
      if sum > 10:
        sum += 1
      else:
        sum += 11
  return sum
 
#game
while (True):
  #makes hands
  for i in range(2):
    addToHand(hand)
    addToHand(dHand)
  
  #inputting the bet
  bet = float(input("You currently have $" + str(money) + ". How much would you like to bet? $"))
  if (bet > money):
    print("You do not have that much money!\n")
  elif (bet <= 0):
    print("You can't bet negative money!")
  else:
    #printing the hands
    print("Dealer's hand: ")
    print("[" + str(dHand[0]) + ", closed card]")
    
    print("Here is your hand:")
    print(hand)
    
    #checking if blackjack was dealt
    if handSum(dHand) == 21 and handSum(hand) == 21:
      print("You both got blackjack! That's lucky! Push.")
      print(dHand)
    elif handSum(dHand) == 21:
      print("The dealer wins! He was dealt blackjack!")
      print(dHand)
      money -= bet
    elif handSum(hand) == 21:
      print("You win!! You got blackjack!!!! 🥳")
      money += bet * 1.5
    else:
      #player's turn
      while (handSum(hand) < 21):
        turn = input("Type in H to hit or S to stay: ")
        #if hit
        if turn.upper() == "H":
          addToHand(hand)
          print("Here is your new hand: ")
          print(hand)
        #if stay
        elif turn.upper() == "S":
          print("Here is your final hand: ")
          print(hand)
          break
        else:
          print("That's not a valid input!")
      
      #if 21, end turn
      if handSum(hand) == 21:
        print("21! Nice")
          
      #bust, end game    
      if handSum(hand) > 21:
        print("You busted!")
        money -= bet
      else:
        #dealer's turn
        print("Dealer's hand: ")
        
        print(dHand)
        
        while (handSum(dHand) <= 17):
          print("Dealer hits")
          addToHand(dHand)
          time.sleep(1)
          print("Dealer's new hand: ")
          print(dHand)
        
        #check dealer win conditions  
        if handSum(dHand) > 21:
          print("Dealer busts! You win!!")
          money += bet
        elif handSum(dHand) > handSum(hand):
          print("Dealer wins.")
          money -= bet
        elif handSum(dHand) == handSum(hand):
          print("Push")
        else:
          print("You win!")
          money += bet
    
    #check for bankruptcy    
    if money == 0:
      print("You've gone bankrupt!")
      break
    
    #reset    
    print("Press Enter to play again.")  
      
    newGame = input()
    
    hand = []
    dHand = []
    cards = ["Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]