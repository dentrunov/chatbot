# -*- coding: utf-8 -*-
import random, time
had_learnt = False
#replys = ['привет', 'как тебя зовут?', 'как дела?', 'пока']
#answers = [['Здравствуйте','Привет','Хеллоу','Здорово','И тебе не хворать'], ['Робот'], ['Неплохо'], ['До свидания']]

with open('ans.txt', encoding='UTF-8') as ansfile:
    answers = []
    for st in ansfile:
        st = st.replace('\n', '')
        answers.append(st.split(','))

with open('rep.txt', encoding='UTF-8') as repfile:
    replys = []
    for st in repfile:
        st = st.replace('\n', '')
        replys.append(st)

def exit_proc():
    global replys
    global answers
    with open('ans.txt', 'w', encoding='UTF-8') as ansfile:
        for item in answers:
            it = str(item)[1:-1].replace("'","")
            ansfile.write(it)
            ansfile.write('\n')

    with open('rep.txt', 'w', encoding='UTF-8') as repfile:
        for item in replys:
            repfile.write(item)
            repfile.write('\n')

def learn(an):
    global replys
    global answers
    global had_learnt
    replys.append(an)
    print('Придумайте ответ:', end=' ')
    answers.append([input()])
    had_learnt = True
    print('Запомнил!')

def password(x):
    if x == '123':
        return True

def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index]))
        if answer == 'пока':
            if had_learnt:
                exit_proc()
            game = False
    else:
        print('Не понимаю')
        if password(input('Введите пароль')):
            learn(answer)
        else:
            print('Невозможно обучить')
    time.sleep(0.5)
    return game


def main():
    gameloop = True
    while gameloop:
        print('Вы: (для выхода напишите "пока")')
        rep = input().lower()
        gameloop = reply(rep)

if __name__ == '__main__':
    main()