# Saving and reading the scores

def save_score(name, score):
    # "a" adds to the file instead of erasing it
    file = open("scores.txt", "a", encoding="utf-8")
    file.write(name + " - " + str(score) + "\n")
    file.close()


def get_scores():
    try:
        file = open("scores.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        # no scores yet
        return []
