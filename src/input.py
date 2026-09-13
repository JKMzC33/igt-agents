import random
def human_choice():
    while True:
        inp = input("Choose a card: A, B, C, D: ").strip().upper()
        if inp in ("A", "B", "C", "D"):
            break
    return inp

def bot_choice():
    return random.choice(("A", "B", "C", "D"))