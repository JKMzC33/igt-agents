from get_data import save_history

def engine(X,  debt):
    diff = X[0] - X[1]
    debt -= diff
    return debt

def Iowatest(game_id,decks,n,debt,choice_func):
    positions = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    history = []
    for i in range(1, n + 1):
        choice = choice_func()
        card = decks[choice][positions[choice]]
        debt = engine(card, debt)
        history.append(save_history(game_id, i, choice, card[0], card[1], debt))
        positions[choice] += 1
    return history
