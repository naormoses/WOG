

def add_Score(difficulty):
    score = difficulty * 3 + 5
    with open('scores.txt', 'r+') as scores_file:
        current_score = scores_file.readline()
        if current_score:
            with open('scores.txt', 'w') as scores_file:
                scores_file.write(str(int(current_score) + score))
        else:
            scores_file.write(str(score))


# if __name__ == '__main__':
#     add_Score(5)
