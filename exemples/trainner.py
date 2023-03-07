from simpleclassifier import Trainner

trainner = Trainner()

trainner.readPatterns("patterns.txt")
print(trainner.model.patterns)
trainner.saveModel()