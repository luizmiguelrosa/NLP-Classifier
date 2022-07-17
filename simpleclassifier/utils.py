PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

processText = lambda text: {word for word in text.split() if not word in PUNCTUATION}

process_similarity = lambda input, pattern: len(input.intersection(pattern)) / len(pattern)