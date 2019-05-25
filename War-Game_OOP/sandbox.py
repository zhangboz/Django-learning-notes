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



my_deck = Deck(SUITE, RANKS)
hand1 = Hand(my_deck.distribute1())
hand2 = Hand(my_deck.distribute2())

P1 = Player("player1",hand1)
P2 = Player("player2",hand2)
game_over = P1.check_empty() and P2.check_empty()
rounds = 1

while game_over == False:
    print("----Round ", rounds,"----")
    print("----Here Is Your Hand----")
    print(P1.player_hand)
    print("----You have ", P1.player_hand.hand_length, " Cards.----")
    played_card_2 = random.choice(P2.player_hand.cards)
    print("----PLEASE: Enter the card you want to play in folloing format. EX: to play Spade A, enter S 14.----")
    user_input = input().upper().split()
    played_card_1 = [user_input[0]]
    played_card_1.append(user_input[1])
    P1.play_card(played_card_1)
    P2.play_card(played_card_2)
    cards_on_table =[]
    cards_on_table.append(played_card_1)
    cards_on_table.append(played_card_2)
    print("----Player 1 played {}{}, Player 2 played {}{}----".format(played_card_1[0],played_card_1[1],played_card_2[0],played_card_2[1]))
    
    if int(played_card_1[1]) > int(played_card_2[1]):
        for item in cards_on_table:
            P1.player_hand.add_card(item)
    elif int(played_card_1[1]) < int(played_card_2[1]):
        for item in cards_on_table:
            P2.player_hand.add_card(item)
    elif int(played_card_1[1]) == int(played_card_2[1]):
        draw = True
        print("----Battle Starts!----")
        while draw == True:            
            i = 0
            while i<3:
                cards_on_table.append(P1.player_hand.cards[0])
                P1.play_card(P1.player_hand.cards[0]) 
                cards_on_table.append(P2.player_hand.cards[0])
                P2.play_card(P2.player_hand.cards[0])         
                i= i+1
            print("Cards on Table are: ",Hand(cards_on_table))
            battle_card_1 = P1.player_hand.cards[0]
            P1.play_card(battle_card_1)
            cards_on_table.append(battle_card_1)
            battle_card_2 = P2.player_hand.cards[0]
            P2.play_card(battle_card_2)
            cards_on_table.append(battle_card_2)
            print("Battle Card 1: {}{}, Battle Card 2: {}{}".format(battle_card_1[0],battle_card_1[1],battle_card_2[0],battle_card_2[1]))
            if int(battle_card_1[1]) > int(battle_card_2[1]):
                draw = False
                print("player 1 wins battle") 
                for item in cards_on_table:
                    P1.player_hand.add_card(item) 
            elif int(battle_card_1[1]) < int(battle_card_2[1]):
                draw = False
                print("player 2 wins battle") 
                for item in cards_on_table:
                    P2.player_hand.add_card(item)       
    rounds = rounds + 1
