secretw = raw_input("Enter your secret word:")
print ("You entered: {}".format(secretw))
offensive = raw_input("Enter you offensive word:")


def offensive_subword(secretw, offensive):
	lastmatch = 0
	match = ""
	for i in range(len(offensive)):
		#print offensive[i]
		print ("search remaining {}: {}".format(secretw, secretw[lastmatch:len(secretw)])) 
		for j in range(lastmatch, len(secretw)):
			if secretw[j] == offensive[i]:
				
				match = match + offensive[i]
				lastmatch = j+1
				#print ("this is the match so far: {}".format(match))
				break

	if match == offensive:
		return True
	else:
		return False


if offensive_subword(secretw, offensive):
	print("***RESULT***")
	print("'{}' can be found inside '{}'".format(offensive, secretw))
else:
	print("***RESULT***")
	print("This word is safe to use!")