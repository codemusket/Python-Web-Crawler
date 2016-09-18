spear = 'as i remember, adam, it was upon this fashion bequeathed me by will but poor a thousand crowns, and, as thou sayest, charged my brother, on his blessing, to breed me well: and there begins my sadness. my brother jaques he keeps at school, and report speaks goldenly of his profit: for my part, he keeps me rustically at home, or, to speak more properly, stays me here at home unkept; for call you that keeping for a gentleman of my birth, that differs not from the stalling of an ox? his horses are bred better; for, besides that they are fair with their feeding, they are taught their manage, and to that end riders dearly hired: but i, his brother, gain nothing under him but growth; for the which his animals on his dunghills are as much bound to him as i. besides this nothing that he so plentifully gives me, the something that nature gave me his countenance seems to take from me: he lets me feed with his hinds, bars me the place of a brother, and, as much as in him lies, mines my gentility with my education. this is it, adam, that grieves me; and the spirit of my father, which i think is within me, begins to mutiny against this servitude: i will no longer endure it, though yet i know no wise remedy how to avoid it.'

trans = str.maketrans('.:;,','    ')
shakes = spear.translate(trans)
shakespear = shakes.split()

def count_word_frequency(word_list):
	freq = {}
	for w in word_list:
		if freq.get(w) == None:
			freq[w] = 1
		else:
			freq[w] += 1
	return freq


print(count_word_frequency(shakespear))
