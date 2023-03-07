from simpleclassifier.utils import *

class Model(object):
    def __init__(self, acceptable:float = 0.55, learn:float = 0.20, dir:str = "model.pkl"):
        """A model of learned patterns to be classified.

        Args:
            acceptable (float, optional): The acceptable value to understand as similar. Defaults to 0.55.
            learn (float, optional): The acceptable value to learn a pattern. Defaults to 0.20.
            dir (str, optional): The model directory. Defaults to "model.pkl".
        """
        self.patterns:dict = {}
        self.acceptable = acceptable
        self.learn = acceptable + learn
        self.dir = dir
    
    def __str__(self) -> str:
        return f"<Model [patterns: {self.returnAmount()}, acceptable: {self.acceptable}, learn: {self.learn}, dir: '{self.dir}']>"
    
    def returnAmount(self):
        count = 0
        for p in self.patterns:
            count += len(self.patterns[p])
        return count

class Classifier:
    def __init__(self, model:Model):
        """A simple text classifier that uses similarities between the text and the database to tell which entity is responsible.

        Args:
            model (Model): The model that will be used for classify.
            learned (dict): All new patterns learned in classification.
        """
        self.model = model
        self.learned = {}
    
    def predict(self, input:set) -> bool | tuple:
        """Predicts the entity responsible for the input using the patterns

        Args:
            input (set): Input processed by method `simpleclassifier.processText`

        Returns:
            boolean | tuple: A boolean value or a tuple with the responsible entity and its similarity
        """
        similaties = self.process_similaties(input)

        probaly = False
        if len(similaties) > 0:
            for action in similaties:
                if not probaly or action[1] > probaly[1]:
                    probaly = action

            if probaly[1] >= self.model.learn and not input in self.model.patterns[probaly[0]]:
                self.learned[probaly[0]] = [] if not probaly[0] in self.learned else self.learned[probaly[0]]
                self.learned[probaly[0]].append(input)
                if not input in self.model.patterns[probaly[0]]:
                    self.model.patterns[probaly[0]].append(input)

        return probaly
    
    def process_similaties(self, input:set) -> list:
        """Performs the process of filtering pattern similarities

        Args:
            input (set): Input processed by method `simpleclassifier.processText`

        Returns:
            list: result of similarities filtering
        """
        similaties = []

        for action in self.model.patterns:
            similaties.append((action, 0))
            i = len(similaties)-1
            for pattern in self.model.patterns[action]:
                similaty = calcu_similaty(input, pattern)
                if similaty >= self.model.acceptable and similaty > similaties[i][1]:
                    similaties[i] = (action, similaty)
                elif similaty == 1.0:
                    break
            if not similaties[i][1]:
                similaties.pop(i)

        return similaties

class Trainner:
    def __init__(self, model:Model = Model()):
        """A simple trainer to store the patterns in your model.

        Args:
            model (Model, optional): The model that will be used for training, which may or may not exist. Defaults to Model().
        """
        self.model = model

    def addPattern(self, action:str, pattern:str):
        self.model.patterns[action].append(processText(pattern))

    def train(self, action:str, pattern:str):
        self.model.patterns[action] = [] if not action in self.model.patterns else self.model.patterns[action]
        self.addPattern(action, pattern)
    
    def readPatterns(self, path:str, marker:str = "*"):
        """Reads a .txt document with training patterns.

        Args:
            path (str): Directory of document.
        """
        with open(path, "r", encoding="utf8") as file:
            current_action = ""
            for row in file.readlines():
                if marker in row[0]:
                    current_action = row[1:].strip("\n")
                else:
                    self.train(current_action, row)

    def saveModel(self):
        """Save the model in a pickle document.
        """
        with open(self.model.dir, "wb+") as f:
            pickle.dump(self.model, f)