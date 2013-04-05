import random

#emilywang
#softdes spring 2013
#functional programming
#blackjack

#making a deck 
def makedeck(howmanydecks=1):
	deck = [] #initial value of deck
	#an element of deck... 	[name of suit, [name of card, vlaue of card]]
	#					 	[string, [string, integer]]

	
	#each element of the name lists is.. [name of thingy is a string, its value is an integer]
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [['Ace', 1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10], ['Jack', 10], ['Queen', 10], ['King', 10]]	
	#rank_name_dictionary = {'Ace':1, '2':2....}
	n = 0 #initial value for how many decks you want to make in this pile
	while n < howmanydecks: 
		for suit in suit_names:
			some_suit = []
			for rank in rank_names:
				some_suit.append([suit, rank])
			deck.append(some_suit)
			#print (some_suit)
		n += 1
			
	print ("This contains " + str((len(deck)/4)) + " decks.")
	return deck #a list


def bj_move (deck, person, currenttotal, decision):
	if person == 'player':
		if decision == 'hit':
			print ()
			print ('Hit!')
			playercard = random.choice(random.choice(deck))
			playercardname = str(playercard[1][0]) + ' of ' + playercard[0]
			print ('You got a ' + playercardname)

			newtotal = currenttotal + playercard[1][1]
			print ('You now have a hand of ' + str(newtotal) + '.')
			return newtotal

		if decision == 'stand':
			print ()
			print ('Stand!')
			print ('As promised, you still have a hand of ' + str(currenttotal) + ".")
			return currenttotal

	if person == 'dealer':
		if decision == 'stand':
			print ("The dealer must stand.")
			return currenttotal
		else: 
			print ("The dealer shall hit.")
			dealercard = random.choice(random.choice(deck))
			newtotal = currenttotal + dealercard[1][1]
			return newtotal


def takingturns(deck, current, currenttotal):
	if current == 'player':
		print ()
		print ("Now, what will you do- hit or stand? A 'hit' is to take another card in hopes of getting closer but not exceeding 21. A 'stand' is to do nothing in hopes that you'll beat the dealer with your current hand. Choose wisely.")
		decision = str(input("Type 'hit' or 'stand' into the computer."))		
		currenttotal = bj_move (deck, current, currenttotal, decision)		
		return currenttotal, decision
	if current == 'dealer':
		print ()
		print ("Dealer's turn!")
		if currenttotal >= 17:
			decision = 'stand'
		if currenttotal <= 16:
			decision = 'hit'
		currenttotal = bj_move (deck, current, currenttotal, decision) 
		return currenttotal, decision


def game_over(playerturn, dealerturn):
	
	#unpacking the variables
	playercurrenttotal = playerturn[0]
	playerchose = playerturn[1]
	dealercurrenttotal = dealerturn[0]
	dealerchose = dealerturn[1]

	gameovermessage = ('\n' + "Game over." + '\n' + "Dealer hand total:" + str(dealercurrenttotal) + '\n' + "Your hand total: " + str(playercurrenttotal)) 

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


def blackjacking ():
	deck = makedeck(4) 	#this game is using 4 decks! 
	print ()
	welcome = """Hi there! Let's play Blackjack! No money bets though! By the way, an Ace is worth 1 in this particular program."""
	print (welcome)
	print ()

	startnow = str(input("Press y if you'd like to begin."))
	
	if startnow == 'y':
		print ()
		print ("Yay, let's play! The goal is to have a hand which is higher than the dealer's but does not exceed 21. Now let's see...")
		print ()

		print ("These are your cards (and the sum if you're too lazy to add).")

		playercard1 = random.choice(random.choice(deck))
		playercard1name = str(playercard1[1][0]) + ' of ' + playercard1[0]

		playercard2 = random.choice(random.choice(deck))
		playercard2name = str(playercard2[1][0]) + ' of ' + playercard2[0]

		playercurrenttotal = playercard1[1][1]+playercard2[1][1]

		print ("Card 1: " + playercard1name)
		print ("Card 2: " + playercard2name)
		print ("Current total: " + str(playercurrenttotal)) 

		print ()

		dealercard1 = random.choice(random.choice(deck))
		dealercard1name = str(dealercard1[1][0]) + ' of ' + dealercard1[0]
		
		dealercard2 = random.choice(random.choice(deck))
		dealercard2name = str(dealercard1[1][0]) + ' of ' + dealercard1[0]

		dealercurrenttotal = dealercard1[1][1]+dealercard2[1][1]

		print ("You're allowed to see one of the dealer's cards.")
		print ("Dealer's card: " + dealercard1name)

		# #player's first turn after deal
		# playerturn = takingturns (deck, 'player', playercurrenttotal)
		# #dealer's first turn after deal
		# dealerturn = takingturns (deck, 'dealer', dealercurrenttotal)
		# checkpoint = game_over(playerturn, dealerturn)
		# # print ("checkpoint is:")
		# # print (checkpoint)

		checkpoint = False

		while checkpoint == False:
			playerturn = takingturns (deck, 'player', playercurrenttotal)
			dealerturn = takingturns (deck, 'dealer', dealercurrenttotal)
			checkpoint = game_over(playerturn, dealerturn)
			
	else: #the person didn't type y to start the game.
		print ("Invalid key press. Restart the program if you'd like to play!")

blackjacking()