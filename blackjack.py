
import random

def get_card():
  cards = [i for i in range(1, 14)]
  return random.choice(cards)

def print_user_result(user, comp):
  print("Your cards: {}, current score: {}".format(user, sum(user)))
  print("Computer's first card: {}".format(comp[0]))

def print_final_result(user, comp):
  print("Your final hand: {}, final score: {}".format(user, sum(user)))
  print("Computer's final hand: {}, final score: {}".format(comp, sum(comp)))

def start_game():
  user = [get_card(), get_card()]
  comp = [get_card()]
  return user, comp

def main():
  is_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':" )
  while is_start == "y":
    user_score, comp_score = start_game()
    print_user_result(user_score, comp_score)

    user_request = input("Type 'y' to get another card, type 'n' to pass:" )
    while (user_request == "y" and sum(user_score) < 21):
      user_score.append(get_card())
      print_user_result(user_score, comp_score)
      user_request = input("Type 'y' to get another card, type 'n' to pass:" )
    
    if sum(user_score) == 21: # user blackjack
      print_final_result(user_score, comp_score)
      print("Win with a Blackjack :))")
    elif sum(user_score) > 21: # user gg
      print_final_result(user_score, comp_score)
      print("You went over. You lose :(")
    else: # otherwise, computer starts to get cards
      while sum(comp_score) < 17:
        comp_score.append(get_card())

      print_final_result(user_score, comp_score)
      if sum(comp_score) > 21:
        print("Opponent went over. You win :)")
      elif sum(comp_score) == 21:
        print("Lose, opponent has Blackjack :((")
      elif sum(comp_score) == sum(user_score):
        print("Draw :|")
      elif sum(comp_score) < sum(user_score):
        print("You win :)")
      else:
        print("You lose :(")
  
    # ask if start a game once the previous game is done.
    is_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':" )
if __name__ == "__main__":
  main()
