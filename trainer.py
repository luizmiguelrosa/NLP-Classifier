from simpleclassifier import processText
import json

if __name__ == "__main__":
    patterns = {}
    on = 1
    while on > 0:
        input_process = processText(str(input("Input > ")))
        action = str(input("Action > "))
        on = int(input("Continue ? "))

        if not action in patterns:
            patterns[action] = []
        
        patterns[action].append(input_process)
    with open("base.json", "w", encoding="utf8") as f:
        json.dump(patterns, f, ensure_ascii=False)