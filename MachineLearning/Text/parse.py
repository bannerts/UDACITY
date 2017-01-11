from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(Data, FILE = False, STEMMER = True, LANGUAGE = 'english'):
	""" Data (as text by default or file), parse out all text and use stemmer (nltk.stem.snowball.SnowballStemmer). 
	"""
	# Transform Data into content
	if not FILE:
		## remove punctuation
		text_string = Data.translate(string.maketrans("", ""), string.punctuation)
	else:
		## Data is a file
		Data.seek(0)  ### go back to beginning of file (annoying)
		all_text = Data.read()
		### split off metadata
		content = all_text.split("X-FileName:")
		if len(content) > 1:
			## remove punctuation
			text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
	words = ''
	stemmer = SnowballStemmer(LANGUAGE)
	for word in string.split(text_string):
		if STEMMER:
			stem_word = stemmer.stem(word)
			words = words + stem_word + ' '
		else:
			words += word + ' '
	return words
