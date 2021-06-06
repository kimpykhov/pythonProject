import random as r


answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']


def how_are_you():
    # напишите ваш код здесь
    return r.choice(answers)

print(how_are_you())