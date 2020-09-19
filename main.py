import math
import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack','Queen', 'King', 'Ace']

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                each_card = Card(suit, rank)
                self.all_cards.append(each_card)
                
    def __str__(self):
        total_deck = ''
        for card in self.all_cards:
            total_deck += "\n" + card.__str__()
        return total_deck

    def shuffle(self):
        
        '''
        random.shuffle returns nothing.
        There is no need to return
        '''

        random.shuffle(self.all_cards)
        
    def deal(self):
        return self.all_cards.pop()
    
class Hand():
    #Increasing value and handling aces
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    #Betting chips
    def __init__(self, total=100):
        
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet?"))
        except:
            print("You have not provided an integer. Please input an integer.")
        else:
            if chips.bet>chips.total:
                print("Sorry, you your bet cannot exceed {}".format(chips.total))
            else:
                break
        
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

            

    

    
    
    
    
    
    
    
    
    
    
    
class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"

        

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal())
    player_two.add_cards(new_deck.deal())
    
game_play=True
























#round_num = 0
#while game_play:
    #round_num += 1
    #print(f"Round {round_num}")
    
    #if (len(player_one.all_cards) == 0):
        #print("Player one is out of cards, so player two wins")
        #break
    
    #if (len(player_two.all_cards) == 0):
        #print("Player two is out of cards, so player one wins")
        #break
    
    #player_one_cards = []
    #player_one_cards.append(player_one.remove_one())
    #player_two_cards = []
    #player_two_cards.append(player_two.remove_one())
    
    #at_war_continue=True
    
    #while at_war_continue:
        #if player_one_cards[-1].value > player_two_cards[-1].value:
            #player_one.add_cards(player_one_cards)
            #player_one.add_cards(player_two_cards)
            #at_war_continue = False
            
    
        #elif player_one_cards[-1].value < player_two_cards[-1].value:
            #player_two.add_cards(player_two_cards)
            #player_two.add_cards(player_one_cards)
            #at_war_continue = False
            
        #else:
            #print("WAR situation")
            
            #if len(player_one.all_cards) < 5:
                #print("Player one has insufficient cards, player two wins")
                #game_on = False
                #break;

            #elif len(player_two.all_cards) < 5:
                #print("Player two has insufficient cards, player one wins")
                #game_on = False
                #break;            
               
            #else:
                #for num in range(5):
                    #player_one_cards.append(player_one.remove_one())
                    #player_two_cards.append(player_two.remove_one())