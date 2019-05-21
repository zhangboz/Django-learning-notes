from random import shuffle
import random
# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 11 12 13 14'.split()
class Deck(): #inputs{suites:list, ranks:list}, #attributes{suites:list, ranks:list, whole_deck:list, deck_length:int} #methods: {distribute1(), distribute2()}
    def __init__(self, suites, ranks):
        self.suites = suites    #attributes
        self.ranks = ranks
        self.whole_deck = []
        self.deck_length = len(suites)*len(ranks)
        for s in self.suites:
            for r in self.ranks:
                card_i = []
                card_i.append(s)
                card_i.append(r)
                self.whole_deck.append(card_i)
        random.shuffle(self.whole_deck)
    def distribute1(self):
        distribution1 = self.whole_deck[0:round(0.5*self.deck_length)]
        return distribution1
    def distribute2(self):
        distribution2 = self.whole_deck[round(0.5*self.deck_length):self.deck_length]
        return distribution2
    def __str__(self):
        return "{}".format(self.whole_deck)
    
class Hand(): #inputs{cards:list}  #attributes: {hand_length:int, cards:list}, #methods: {add_card(card:list), remove_card(card:list)}
    def __init__(self,cards):
        self.hand_length = len(cards)
        self.cards = cards
    def add_card(self, card):
        self.cards.append(card)
        self.hand_length = len(self.cards)
    def remove_card(self, card):
        self.cards.remove(card)
        self.hand_length = len(self.cards)
    def __str__(self):
        card_string = ""
        for entry in self.cards:
            card_string = card_string + entry[0] + entry[1]+", "
        return "{}".format(card_string) 

class Player(): #inputs{name:str, hand:Hand}. #attributes:{player_name:str, player_hand:Hand}. #methods{play_card(played_card:list), check_empty()}
    def __init__(self,name,hand:Hand):
        self.player_name = name
        self.player_hand = hand
    def play_card(self,played_card):
        self.player_hand.remove_card(played_card)
    def check_empty(self):
        if self.player_hand.hand_length == 0:
            return True
        else:
            return False


    # """
    # This is the Player class, which takes in a name and an instance of a Hand
    # class object. The Payer can then play cards and check if they still have cards.
    # """

        

    # """
    # This is the Player class, which takes in a name and an instance of a Hand
    # class object. The Payer can then play cards and check if they still have cards.
    # """



    def __init__(self,name,hand:Hand):
        self.player_name = name
        self.player_hand = hand
    def play_card(self,played_card):
        self.player_hand.remove_card(played_card)
    def check_empty(self):
        if self.player_hand.hand_length == 0:
            return True
        else:
            return False


    # """
    # This is the Player class, which takes in a name and an instance of a Hand
    # class object. The Payer can then play cards and check if they still have cards.
    # """

my_deck = Deck(SUITE, RANKS)
hand1 = Hand(my_deck.distribute1())
hand2 = Hand(my_deck.distribute2())

P1 = Player("player1",hand1)
P2 = Player("player2",hand2)
game_over = P1.check_empty() and P2.check_empty
while game_over == False:
    print(P1.player_hand)
    played_card_2 = random.choice(P2.player_hand.cards)
    print(played_card_2)
    print("Enter the card you want to play in folloing format. EX: to play spade A, enter S 14")
    user_input = input().upper().split()
    played_card_1 = [user_input[0]]
    played_card_1.append(user_input[1])
    P1.play_card(played_card_1)
    print("Player 1 played {}{}, Player 2 played {}{}".format(played_card_1[0],played_card_1[1],played_card_2[0],played_card_2[1]))
    if int(played_card_1[1]) > int(played_card_2[1]):
        P1.player_hand.add_card(played_card_1)
        P1.player_hand.add_card(played_card_2)
    elif int(played_card_1[1]) < int(played_card_2[1]):
        P2.player_hand.add_card(played_card_1)
        P2.player_hand.add_card(played_card_2)
    elif int(played_card_1[1]) == int(played_card_2[1]):
        i = 0
        cards_on_table =[]
        while i<3:
            cards_on_table.append(P1.player_hand.cards[0])
            P1.play_card(P1.player_hand.cards[0]) 
            cards_on_table.append(P2.player_hand.cards[0])
            P2.play_card(P2.player_hand.cards[0])         
            i= i+1
            print(cards_on_table)
