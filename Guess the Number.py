# Игра Угадай число

import random       # Для генерации случайного числа

lowDigit = 10       # Нижняя граница случайного числа
highDigit = 50      # Верхняя граница случайного числа
digit = 0           # Загаданное компьютером число

countInput = 0      # Количество попыток угадать
win = False         # Угадал текущее число?
playGame = True     # Продолжается ли игра?
x = 0               # Число которое вводит пользователь
startScore = 100    # Начальное количество очков
score = 0           # Текущее количество очков
maxScore = 0        # Максимальное за сессию игры


# ====================================================

# ---- ОСНОВНОЙ ЦИКЛ
while playGame:

    # ----------------------------------------------------

    # Определение угадываемого числа
    digit = random.randint(lowDigit, highDigit)

    # ----------------------------------------------------

    # Начальные настройки

    score = startScore
    countInput = 1

    # Приветствие
    print("=" * 60)
    print(f"Компьютер загадал целое число от {lowDigit} до {highDigit} включительно,",
          "Попробуйте отгадать!", sep='\n',)
    print()
    print(f'Рекорд: {maxScore}')
    print("=" * 60)

    # ----------------------------------------------------

    # Запрос числа

    # ---- ВНУТРЕННИЙ ЦИКЛ запроса числа

    while not win and score > 0:  # Пока win равен False и количество очков больше 0
        print(f'Очков: {score}')
        print(f'Номер попытки: {countInput}')

        # --------------------------------------------------------------
        # Запрос у пользователя числа и его проверка

        # ---- ВНУТРЕННИЙ ЦИКЛ проверки числа
        x = ""  # Задаём заведомо неверное значение для переменной "х"
        while not x.isdigit():  # Пока значение "х" неверное
            x = input(f"Ввведите, число от {lowDigit} до {highDigit}: ")  # Спрашиваем число
            if not x.isdigit():  # Если не число
                print("." * 27 + "Введите, пожалуйста, число")  # Просим ввести число
        # ---- КОНЕЦ ВНУТРЕННЕГО ЦИКЛА проверки числа

        x = int(x)  # Преобразовать тип значения "х" из строкового в числовой

        if x == digit:  # Проверяем число на совпадение с загаданным, Если число совпадает с загаданным,
            win = True  # Засчитываем победу
            # ---- КОНЕЦ ЦИКЛА по причине победы
        else:
            # --------------------------------------------------------------------------
            # Блок подсказок
            if countInput > 1:
                if input('Нужна подсказка? 1 - да, 2 - нет: ') == '1':
                    if 2 < countInput < 5:
                        score -= 2
                        if digit > x:
                            print('Загаданное число больше последнего введённого')
                        else:
                            print('Загаданное число меньше последнего введённого')
                    elif countInput == 5:
                        score -= 4
                        if digit % 4 == 0:
                            print('Загаданное делится на 4')
                        else:
                            print('Загаданное не делится на 4')
                    elif countInput == 6:
                        score -= 8
                        if digit % 3 == 0:
                            print('Загаданное делится на 3')
                        else:
                            print('Загаданное не делится на 3')
                    elif countInput >= 7:
                        score -= 10
                        if digit % 2 == 0:
                            print('Загаданное число чётное')
                        else:
                            print('Загаданное число нечётное')

            # Конец блока подсказок
            # --------------------------------------------------------------
                        score -= 5
            countInput += 1
        print("-" * 60)

    if win is True:  # Проверка на условие победы
        print("Правильно! Победа!")
        # Проверка на рекорд по очкам
        if score > maxScore:  # Если количество очков больше текущего рекорда
            maxScore = score  # Обновляем рекорд
            print('Вы поставили новый рекорд по очкам!')
            print(f'Рекорд: {maxScore}')
    else:
        print('Очки закончились!',
              'Вы проиграли :(!', sep='\n')

    # ---- КОНЕЦ ВНУТРЕННЕГО ЦИКЛА запроса числа

    if input("Enter - сыграть ещё, '0' - выход: ") == '0':
        print('Спасибо за игру! Приходите ещё!')
        playGame = False
    else:
        win = False
# ---- КОНЕЦ ОСНОВНОГО ЦИКЛА
