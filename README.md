# NLP Classifier
A simple text classifier that uses similarities between the text and the database to tell which entity is responsible.

### Requirements:
Python 3.7 - NLTK - JSON

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