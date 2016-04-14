import sys

card_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		cards = test.split(' ')
		c1_value = card_map[cards[0][:-1]]
		c1_suit = cards[0][-1]
		c2_value = card_map[cards[1][:-1]]
		c2_suit = cards[1][-1]
		
		# a > b print a
		if c1_value > c2_value:
			if c2_suit == cards[3].strip() and c1_suit != cards[3].strip():
				print cards[1]
			else:
				print cards[0]
		# a == b print both
		elif c1_value == c2_value:
			if c2_suit == cards[3].strip() and c1_suit != cards[3].strip():
				print cards[1]
			else: 
				print cards[0],
				if not (c1_suit == cards[3].strip() and c2_suit != cards[3].strip()):
					print cards[1]
				else:
					# need to print new line in case of only printing cards[0]
					print ''
		# a < b print b
		else:
			if c1_suit == cards[3].strip() and c2_suit != cards[3].strip():
				print cards[0]
			else:
				print cards[1]
