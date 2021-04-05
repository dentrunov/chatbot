# -*- coding: utf-8 -*-
import time, random

repfile = open('rep.txt', encoding="utf-8")
ansfile = open('ans.txt', encoding="utf-8")



replys = repfile.readlines()
repfile.close()

# ответы бота
answers = ansfile.readlines()
for i in range(len(answers)):
    answers[i] = answers[i].split(',')
ansfile.close()
print(answers)









def learn(an):
    global replys
    global answers
    replys.append(an)
    print('Придумайте ответ:', end=' ')
    r = input()
    answers.append([r])


def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index]))
        if answer == 'пока':
            game = False
    else:
        print('Не понимаю')
        learn(answer)
    time.sleep(0.5)
    return game


def main():
    gameloop = True
    while gameloop:
        print('Вы:')
        rep = input().lower()
        gameloop = reply(rep)

if __name__ == '__main__':
    main()