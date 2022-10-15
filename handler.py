import json
from spellchecker import SpellChecker

spell = SpellChecker()

def hello(event: dict, context):


    body = {
        "correction": spell.correction(event["word"]),
    }

    return {"statusCode": 200, "body": json.dumps(body)}
