from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "I want to find a restaurant in Mumbai"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))