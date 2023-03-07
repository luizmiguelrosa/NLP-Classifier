import pickle

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

processText = lambda text: {word for word in text.split() if not word in PUNCTUATION}
calcu_similaty = lambda input, pattern: len(pattern.intersection(input)) / len(pattern)

def readModel(dir:str):
    with open(dir, "rb") as f:
        return pickle.load(f)