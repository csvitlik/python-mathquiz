# Decks

A deck is a comma separated value (csv) file.

The first line of the deck is the field names, starting from index 0:

	% sed 1q math-1x1-20x20.deck
	Question,Answer

The field names are displayed in a tabular format:

	% sed 2q math-1x1-20x20.deck
	Question,Answer
	1x1=?,1

Would be displayed as:

| Question | Answer |
| --------:| ------:|
| 1x1=?	   | 1	    |