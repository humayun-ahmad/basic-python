# solution 1:

with open("word.txt",'r') as f:
	word_file = f.read().splitlines()
	

with open("sentence.txt",'r') as f:
	sentence_file = f.read().splitlines()
	for line in sentence_file:
		for word in word_file:
			if word in line:
				print(line)
				break

# solution 2:

with open("word.txt") as f:
    key_words = set(f.read().splitlines())

# reading file2 and iterating over all read lines 
with open("sentence.txt") as f:
    all_lines = f.read().splitlines()
    for line in all_lines:
        if any(kw in line for kw in key_words): # if any of the word in key words is in line print it
            print(line)
