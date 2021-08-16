import re
import requests


def find_definition(word: str):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    response_status = response.status_code
    if response_status != 200:
        return "No definitions found"
    json_response = response.json()
    meaning = json_response[0]['meanings'][0]
    part_of_speech = meaning['partOfSpeech']
    definition = meaning['definitions'][0]['definition']
    return f"Output: {word.capitalize()}. {part_of_speech.capitalize()}. {definition.capitalize()}"


if __name__ == '__main__':
    word = input("Word? ").strip()
    word_expression = re.compile("[a-zA-Z]+")
    while not word_expression.fullmatch(word):
        word = input("Enter a valid Word? ").strip()
    print(find_definition(word))