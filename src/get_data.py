import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def save_history(game_id, i, choice, reward, penalty, debt):
    return [game_id, i, choice, reward, penalty, debt]

def save_to_csv(history):
    df = pd.DataFrame(history, columns=["game_id", "trial", "choice", "reward", "penalty", "debt"])
    df.to_csv(BASE_DIR / "data" / "game_history.csv", index=False)