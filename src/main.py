import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "info.yml", "r") as f:
    config = yaml.safe_load(f)

def engine(X,  balance):
    diff = X[0] - X[1]
    balance -= diff
    return balance

def Iowatest(decks,n,debt):
    positions = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for i in range(n):
        while True:
            inp = input("Choose a card: A, B, C, D: ").strip().upper()
            if inp in ("A", "B", "C", "D"):
                break
            print("Niepoprawny wybór. Wpisz A, B, C lub D.")
        debt = engine(decks[inp][positions[inp]], debt)
        print(f"+{decks[inp][positions[inp]][0]}, -{decks[inp][positions[inp]][1]} Debt: {debt}")
        positions[inp] += 1
    print(f"You finished with Debt: {debt}")

decks = config["decks"]
Iowatest(decks, config["number_of_trials"], config["starting_balance"])
