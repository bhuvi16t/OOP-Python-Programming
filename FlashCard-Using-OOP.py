# Build flashcard using class in Python.
# Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.
# 
# Approach:

# Create a class named FlashCard.
# Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
# Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
# Now prompt the user to answer the color of the randomly chosen fruit.
# If correct print correct else print wrong
# write your code here


import random
class FlashCard:
  def __init__(self):
    # basic structure 
    self.fruitname = {"Banana": "yellow", "Strawberries": "pink","Apple":"red","Mango":"yellow"}
    self.fruit = random.choice(list(self.fruitname.keys()))
    self.color = self.fruitname[self.fruit]
    self.Quiz()
  # quiz method 
  def Quiz(self):
    print('Welcom to the Fruit quize')
    print(f'What is the color of :{self.fruit}')
    user_input = input('Enter the color here ')
    if user_input == self.color:
      print('Correct answer')
    else:
      print('Wrong answer')
    ply = input('Enter 0, if you want to play again:')
    if ply == '0':
      self.fruit = random.choice(list(self.fruitname.keys()))
      self.color = self.fruitname[self.fruit]
      self.Quiz()
    else:
      print('Thank you')
      
obj = FlashCard()

 
