<h1 align="center">NLP Classifier</h1>
A simple text classifier that uses similarities between the text and the database to tell which entity is responsible.

### Requirements:
Python 3.7 - NLTK - JSON

### How to use:
```python
# First, import the labries
import json, import simpleclassifier
```


```python
# Second, open the database
with open("base.json", "r", encoding="utf8") as f:
    patterns = json.load(f)
```

```python
# Third, process your input
input_process = simpleclassifier.processText(str(input("Input > ")))
```

```python
# Fourth, create the classifier and predict output
classifier = simpleclassifier.Classifier()

output = classifier.predict(patterns, input_process)
```


### Database:
```json
base.json


{
    "wikipedia": [
        [
            "quem",
            "foi"
        ],
        [
            "quem",
            "é"
        ],
        [
            "quando",
            "foi"
        ],
        [
            "quando",
            "foi",
            "que"
        ],
        [
            "quando",
            "é"
        ],
        [
            "onde",
            "foi"
        ],
        [
            "onde",
            "é"
        ],
        [
            "o",
            "que",
            "é"
        ]
    ],
    "calculadora": [
        [
            "quanto",
            "é"
        ]
    ],
    "relogio": [
        [
            "quantas",
            "horas",
            "são"
        ],
        [
            "que",
            "horas",
            "são"
        ]
    ]
}
```