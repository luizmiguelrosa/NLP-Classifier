from simpleclassifier import Classifier, readModel, processText

model = readModel("model.pkl")
classifier = Classifier(model)

input = processText("Quem foi Santos Dummont")
result = classifier.predict(input)
print(result)