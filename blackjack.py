import random
values = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')

class Card:
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__ (self):
        return self.rank + " of " + self.suit
        
class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
                
    def shuffle (self):
        random. shuffle (self.allcards)
        
    def deal_one(self):
        return self.allcards.pop ()
    
class Player:
    
    def __init__ (self,name):
        self.name = name
        self.allcards = []
        
    def add_cards (self,new_cards):
            self.allcards.append(new_cards)
            
    def __str__ (self):
        if(self.name!='Computer'):
            stre = ''
            for i in range(len(self.allcards)):
                stre = stre + (f'{self.name} has {self.allcards[i].rank} of {self.allcards[i].suit} cards ({self.allcards[i].value}) \n')
            return stre
        else:
            stre = 'Card 1 is hidden \n'
            for i in range(0,len(self.allcards)):
                if i != 1:
                    stre = stre + (f'{self.name} has {self.allcards[i].rank} of {self.allcards[i].suit} cards ({self.allcards[i].value}) \n')
            return stre

class Chips:

    def __init__ (self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -=self.bet

def take_bet (chips):
    chips.bet = 10000
    try:
        chips.bet = int(input('How many chips do you wanna bet ? \n'))
    except:
        print('Sorry please provide an integer. \n')
        take_bet(chips)
    else:
        while chips.bet > chips.total:
            print(f'Sorry you do not have enough chips. You have: {chips.total} \n')
            take_bet(chips)

def checkace(card_value1):
    if ((Player1.allcards[0].rank) == 'Ace'):
        if (int(input('Pick the value for Ace [1/11]')) == 11):
            card_value1 = card_value1 + 10
    if ((Player1.allcards[1].rank) == 'Ace'):
        if (int(input('Pick the value for Ace [1/11]')) == 11):
            card_value1 = card_value1 + 10

def showcards():
    print(f"\n Player's Hand : \n{Player1}")
    print(f"Dealer's Hand : \n{Player2} \n ")
    
inname = input('Enter Your Name: ')
chips = Chips(500)
playon = True

while playon == True:
    print ('\n WELCOME TO BLACKJACK \n')
    newdeck = Deck()
    newdeck.shuffle()
    take_bet(chips)
    Player1 = Player(inname)
    Player2 = Player('Computer')
    Player1.add_cards (newdeck.deal_one())
    Player1.add_cards (newdeck.deal_one())
    Player2.add_cards (newdeck.deal_one())
    Player2.add_cards (newdeck.deal_one())

    print(Player1)
    print(Player2)
    blackjack1 = True
    blackjack2 = True
    card_value1 = Player1.allcards[0].value+Player1.allcards[1].value
    card_value2 = Player2.allcards[0].value+Player2.allcards[1].value
    checkace(card_value1)
    card_number = 1

    while blackjack1 == True:
        print(f'Sum of Cards = {card_value1}')
        inp = ''
        while inp not in ['H','S','h','s']:
            inp = input('Want to Hit or Stand? [H/S]')
        if inp.upper() == 'H':
            Player1.add_cards(newdeck.deal_one())
            card_number += 1
            print(f'Card added {Player1.allcards[card_number].value}')
            card_value1 = card_value1 + Player1.allcards[card_number].value
        else:
            blackjack1 = False
        
    cardnumber = 2
    while blackjack2 == True:
        if(card_value2<=17):
            Player2.add_cards(newdeck.deal_one())
            print(f'Card added {card_value2}')
            card_value2 = card_value2 + Player2.allcards[cardnumber].value
            cardnumber +=1
        else: 
            blackjack2 = False

    if(card_value1 <= 21 and ((card_value1 > card_value2)) or card_value2>21):
        chips.win_bet()
        print(f'\n{Player1.name} Won\n')
        showcards()
    elif (card_value1 == card_value2):
        print(f'\nPush Tie\n')
    else:
        chips.lose_bet()
        print(f'\n{Player2.name} Won\n')
        showcards()
    
    if(input('Wanna Play Again? [Y/N]: \n').upper() == 'Y'):
        playon = True
        del Player1
        del Player2
    else: playon = False