import random

#emilywang
#softdes spring 2013
#object oriented programming
#blackjack

class Card(object):
	"This is a playing card."

	#class attributes, dictionary version
	# suit_names = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
	# rank_names = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack',  12:'Queen', 13:'King'}

	#class attributes, list version
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self,suit=0,rank=2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	# def cardvalue(self):
	# 	return 	

class BJDeck(object):
	"""This BJDeck contains four standard decks' worth of cards. Stands true to the tradition of using multiple decks in Blackjack."""
	def __init__(self):
		self.cards = []
		n = 0
		while n < 4:
			for suit in range(4):
				for rank in range(1,14):
					card = Card (suit,rank)
					self.cards.append(card)
			n = n + 1 

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def currenttotal(self):
		sum_value = 0
		for card in self.cards:
			if card.rank > 10:
				card.rank = 10
			sum_value = sum_value + card.rank
		return sum_value

	def add_card(self, card):
		self.cards.append(card)

	def randomcard(self):
		return random.choice(self.cards)

class Hand(BJDeck):
	"This is a hand of cards. Used by Emily for coding Blackjack with object-oriented programming."

	def __init__(self, label =''):
		self.cards = []
		self.label = label

	def BJdeal (self, deck, num):
		for i in range(num):
			self.add_card(deck.randomcard())

	def p_turn (self, deck, pcurrenttotal):
		currenttotal = pcurrenttotal
		print ()
		print ("Now, what will you do- hit or stand? A 'hit' is to take another card in hopes of getting closer but not exceeding 21. A 'stand' is to do nothing in hopes that you'll beat the dealer with your current hand. Choose wisely.")
		decision = str(input("Type 'hit' or 'stand' into the computer."))
		
		if decision == 'hit':
			print ()
			print ('Hit!')
			playercard = deck.randomcard()
			print ('You got a ' + str(playercard) + '.')

			#calculating new currenttotal
			if playercard.rank > 10:
				playercard.rank = 10
			newtotal = currenttotal + playercard.rank
			print ('You now have a hand of ' + str(newtotal) + '.')
			return newtotal, decision

		if decision == 'stand':
			print ()
			print ('Stand!')
			#currenttotal does not change
			print ('As promised, you still have a hand of ' + (str(currenttotal)) + '.')
			return currenttotal, decision

	def d_turn (self, deck, dcurrenttotal):
		currenttotal = dcurrenttotal
		print ()
		print ("Dealer's turn!")
		if currenttotal <= 16:
			decision = 'hit'
			print ('The dealer shall hit.')
			dealercard = deck.randomcard()
			#print ('dealercard is - deleteme-')
			#print (dealercard)
			if dealercard.rank > 10:
				dealercard.rank = 10
			newtotal = currenttotal + dealercard.rank
			return newtotal, decision
		if currenttotal >= 17:
			decision = 'stand'
			print ('The dealer must stand.')
			#print (currenttotal)
			return currenttotal, decision

def game_over(playerturn, dealerturn):
	
	#unpacking the variables
	playercurrenttotal = playerturn[0]
	playerchose = playerturn[1]
	dealercurrenttotal = dealerturn[0]
	dealerchose = dealerturn[1]

	gameovermessage = ('\n' + "Game over." + '\n' + "Dealer hand total:" + str(dealercurrenttotal) + '\n' + "Your hand total: " + str(playercurrenttotal) + '\n') 

	if playerchose == 'hit':
		if playercurrenttotal == 21:
			if dealercurrenttotal == 21:
				print (gameovermessage)
				print ("Both you and the dealer win. How fortuitous! (or maybe not). Play again?")
				return
			if dealercurrenttotal < 21:
				print (gameovermessage)
				print ("Nice hand! Sir, you are victorious.")  
				return
		if playercurrenttotal < 21 and dealercurrenttotal == 21:
			print (gameovermessage)
			print ("Sir, you have lost. Dealer got a hand of 21 before you did. Play again?")
			return				
		if playercurrenttotal > 21:
			print (gameovermessage)
			print ("Bust! Sir, you have lost. Play again?")
			return
		if dealercurrenttotal > 21:
			print (gameovermessage)
			print ("Dealer bust! Sir, you are victorious.")
			return
		else:
			return False
	if playerchose == 'stand':
		if playercurrenttotal < 21 and dealercurrenttotal == 21:
			print (gameovermessage)
			print ("Sir, you have lost. Dealer got a hand of 21.")
			return 	
		if playercurrenttotal == 21 and dealercurrenttotal == 21:
			print (gameovermessage)
			print ("Both you and the dealer win. How fortuitous! (or maybe not). Play again?")
			return
		if playercurrenttotal < 21 and dealercurrenttotal > 21:
			print (gameovermessage)
			print ("Dealer bust! Sir, you are victorious.")
			return
		if playercurrenttotal == dealercurrenttotal:
			print (gameovermessage)
			print ("Looks like a tie. Play again?")
			return
		if dealerchose == 'stand':
			if playercurrenttotal < dealercurrenttotal:
				print (gameovermessage)
				print ("Alas and alack, the dealer wins. Play again?")
				return
			if playercurrenttotal > dealercurrenttotal:
				print (gameovermessage)
				print ("Sir, you are victorious!")
				return
			else:
				return False
		else:
			return False
	else: 
		return False
		

def oop_bj():

	deck = BJDeck()
	#print ("here's the deck")
	#print (deck)

	welcome = """Hi there! Let's play Blackjack! No money bets though! By the way, an Ace is worth 1 in this particular program."""
	print (welcome)
	print ()

	startnow = str(input("Press y if you'd like to begin."))

	if startnow == 'y':
		print ()
		print ("Yay, let's play! The goal is to have a hand which is higher than the dealer's but does not exceed 21. Now let's see...")
		print ()

		print ("These are your cards (and the sum if you're too lazy to add).")

		playerhand = Hand ('player hand')
		playerhand.BJdeal(deck, 2)
		playercurrenttotal = playerhand.currenttotal()
		print (playerhand)
		print ("Current total: " + str(playercurrenttotal))

		print()

		print ("You're allowed to see one of the dealer's cards.")
		dealerhand = Hand ('dealer hand')
		dealerhand.BJdeal(deck, 2)
		dealercurrenttotal= dealerhand.currenttotal()
		#print (dealerhand)
		#test print
		print ("Dealer's card: " + str(dealerhand.randomcard()))
		#print ("deletemelater Dealer's current total: " + str(dealercurrenttotal))
		print ()

		playerturn = playerhand.p_turn(deck, playercurrenttotal)
		playercurrenttotal = playerturn[0]
		dealerturn = dealerhand.d_turn(deck, dealercurrenttotal)
		dealercurrenttotal = dealerturn[0]
		checkpoint = game_over(playerturn, dealerturn)
		# print ("checkpoint is: ")
		# print (checkpoint)

		while checkpoint == False:
			playerturn = playerhand.p_turn(deck, playercurrenttotal)
			playercurrenttotal = playerturn[0]
			dealerturn = dealerhand.d_turn(deck, dealercurrenttotal)
			dealercurrenttotal = dealerturn[0]
			checkpoint = game_over(playerturn, dealerturn)
			# print ("checkpoint is: ")
			# print (checkpoint)


	else: #the person didn't type y to start the game.
		print ("Invalid key press. Restart the program if you'd like to play!")

oop_bj()