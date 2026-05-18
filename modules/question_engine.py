import json
import random

def load_questions(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_random_question(questions):
    return random.choice(questions)
