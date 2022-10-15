from spellchecker import SpellChecker

spell = SpellChecker()

def correct_word(event: dict, _):
    return {
        "correction": spell.correction(event.get("word"))
    }
