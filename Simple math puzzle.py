import random

lowerBorder = 10  # Lower border for numbers
upperBorder = 100  # Upper border for numbers
sign = 0  # Operational sign (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division)
playGame = True  # Is the game continue
count = 0  # Qty of solved puzzles
right = 0  # Qty of right answers
x, y, z = 0, 0, 0  # Digits
answer = ''  # Player answer
score = 0

# Show greetings
# Show statistics
# Numbers generation
# Sign choose
# Question to player

print('*' * 60)
print('''Компьютер составляет примеры, попробуйте решить.''')

# ---- MAIN CYCLE ----
while playGame:

    # - Greetings -
    print('*' * 60)
    print('''Для завешения работы введите STOP.''')

    print(f'Количество решённых вопросов: {count}')
    print(f'Количество правильных ответов: {right}')
    print(f'Количество набранных очков: {score}')
    print('*' * 60)

    sign = random.randint(1, 4)  # Choosing sign

    if sign == 1:
        # ---- ADDITION BLOCK ---- begin
        z = random.randint(lowerBorder, upperBorder)  # Define answer
        x = random.randint(lowerBorder, z)  # Define x digit
        y = z - x  # Define y digit

        if random.randint(0, 1):
            puzzle = f'{x} + {y} = '
        else:
            puzzle = f'{x} + {y} = '

        # ---- ADDITION BLOCK ---- end

    elif sign == 2:
        # ---- SUBTRACTION BLOCK ---- begin
        x = random.randint(lowerBorder, upperBorder)
        y = random.randint(0, x - lowerBorder)
        z = x - y

        puzzle = f'{x} - {y} = '
        # ---- SUBTRACTION BLOCK ---- end

    elif sign == 3:
        # ---- MULTIPLICATION BLOCK ---- begin
        x = random.randint(1, (upperBorder - lowerBorder) // 5)  # max possible multiplier
        y = random.randint(x, upperBorder) // x
        z = x * y

        if random.randint(0, 1):
            puzzle = f'{x} * {y} = '
        else:
            puzzle = f'{y} * {x} = '
        # ---- MULTIPLYING BLOCK ---- end

    elif sign == 4:
        # ---- DIVISION BLOCK ---- begin
        x = random.randint(1, (upperBorder - lowerBorder) // 5)
        y = random.randint(x, upperBorder) // x
        y = x * y
        z = y // x

        puzzle = f'{y} / {x} = '
        # ---- DIVISION BLOCK ---- end

    # INPUT BLOCK
    answer = ''

    # check input
    while not answer.isdigit()\
            and answer.lower() != 'stop'\
            and answer.lower() != 's'\
            and answer.lower() != 'ыещз'\
            and answer.lower() != 'ы'\
            and answer.lower() != 'help'\
            and answer.lower() != 'h'\
            and answer.lower() != '?'\
            and answer.lower() != 'рудз'\
            and answer.lower() != 'р'\
            and answer.lower() != ',':
        answer = input(f'Введите ответ: {puzzle}')
        if not answer.isdigit() \
            and answer.lower() != 'stop' \
            and answer.lower() != 's' \
            and answer.lower() != 'ыещз' \
            and answer.lower() != 'ы' \
            and answer.lower() != 'help' \
            and answer.lower() != 'h' \
            and answer.lower() != '?' \
            and answer.lower() != 'рудз' \
            and answer.lower() != 'р' \
            and answer.lower() != ',':
            print('.' * 10 + '''Пожалуйста введите число.
    Для завершения работы введите STOP''')
        elif answer.lower() == 'help'\
            or answer.lower() == 'h'\
            or answer.lower() == '?'\
            or answer.lower() == 'рудз'\
            or answer.lower() == 'р'\
            or answer.lower() == ',':
            if z > 9:
                print(f'Последняя цифра ответа: {z % 10}')
                score -= 10
            else:
                print('В ответе одна цифра.')

        elif answer.lower() == 'stop'\
                or answer.lower() == 's'\
                or answer.lower() == 'ыещз'\
                or answer.lower() == 'ы':
            playGame = False
            print('Спасибо за игру! Приходите ещё!')
        else:
            if int(answer) == z:
                count += 1
                right += 1
                score += 10
                print('Правильно!')
            else:
                count += 1
                score -= 20
                print(f'''Ответ неправильный!
Правильно: {z}!
Вы можете ввести HELP, чтобы увидеть подсказку за 10 очков.''')
