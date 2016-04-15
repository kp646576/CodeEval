import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.strip()
		if len(test) > 55:
			trimmed = test[:40]
			if trimmed.find(' ') != -1:
				words = trimmed.split(' ')
				trimmed = ' '.join(words[:-1])
			print trimmed + '... <Read More>'		
		else:
			print test