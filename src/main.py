from get_data import save_to_csv
from game import Iowatest
from input import bot_choice
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "info.yml", "r") as f:
    config = yaml.safe_load(f)

decks = config["decks"]

all_history = []

for game_id in range(1, config["number_of_games"] + 1):
    history = Iowatest(game_id, decks, config["number_of_trials"], config["starting_debt"], bot_choice)
    all_history.extend(history)
save_to_csv(all_history)

