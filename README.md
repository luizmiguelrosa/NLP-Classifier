<h1 align="center">NLP Classifier</h1>
A simple text classifier that uses similarities between the text and the database to tell which entity is responsible.

The classifier documentation: [Documentation](https://github.com/Masso13/NLP-Classifier/wiki)

### Requirements:
Python 3.7 - NLTK
```bash
pip install nltk==3.6.2
```

### How to use:
```python
# First, import the labries
import json, simpleclassifier
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
In line 5 of the simpleclassifier, it has 
```python
stopwords = set(stopwords.words("portuguese") + list(punctuation))
```

Where is "portuguese", put your language to work perfectly.
Consult the NLTK documentation to know which parameter to put.

### Create Database:
```bash
python trainer.py
```
```json
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
