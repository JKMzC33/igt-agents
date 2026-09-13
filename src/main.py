import random
import yaml
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "info.yml", "r") as f:
    config = yaml.safe_load(f)

def human_choice():
    while True:
        inp = input("Choose a card: A, B, C, D: ").strip().upper()
        if inp in ("A", "B", "C", "D"):
            break
    return inp

def bot_choice():
    return random.choice(("A", "B", "C", "D"))

def engine(X,  balance):
    diff = X[0] - X[1]
    balance -= diff
    return balance


def save_history(game_id, i, choice, reward, penalty, debt):
    return [game_id, i, choice, reward, penalty, debt]

def Iowatest(game_id,decks,n,debt,choice_func):
    positions = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    history = []
    for i in range(n + 1):
        choice = choice_func()
        card = decks[choice][positions[choice]]
        debt = engine(card, debt)
        history.append(save_history(game_id, i, choice, card[0], card[1], debt))
        positions[choice] += 1
    return history

def save_to_csv(history):
    df = pd.DataFrame(history, columns=["game_id", "trial", "choice", "reward", "penalty", "debt"])
    df.to_csv(BASE_DIR / "data" / "game_history.csv", index=False)

decks = config["decks"]

all_history = []

for game_id in range(config["number_of_games"] + 1):
    history = Iowatest(game_id, decks, config["number_of_trials"], config["starting_balance"], bot_choice)
    all_history.extend(history)
save_to_csv(all_history)

