from ctypes import *
import time
import random

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


# ---- VARIABLES ----

default_money = 10000  # Total amount of money
currency = 'руб.'  # Currency
visibility = True  # Visibility for service function
result_won = 0  # Won amount of money
play_game = True  # Marker to continue game
money = 0  # variable for current amount of money


# ---- FUNCTIONS ----


def get_input(digit, message):  # This function check user input. Arguments:
    # digit - possible input, message - Motivation text for input
    color(7)
    ret = ''
    while (ret == '') or (ret not in digit):
        ret = input(message)
    return ret

# ===================================================================================================================


def get_int_input(minimum, maximum, message):  # This function check user bid input. Arguments:
    # maximum - max possible bid, minimum - min possible bid, message - Motivation text for input
    color(7)
    ret = -1
    while not (minimum <= ret <= maximum):
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print('    Введите, пожалуйста, число...')
    return ret

# ===================================================================================================================


def load_money():  # This function loads users money amount from the file money.dat
    try:
        f = open('money.dat', 'r')
        m = int(f.readline())
    except FileNotFoundError:
        print(f'Файл не найден. Задано значение по умолчанию: {default_money} {currency}')
        # default_money is a global variable
        m = default_money
    return m

# ===================================================================================================================


def save_money(money_to_save):  # This function will save resulting money amount to the file money.dat
    # Arguments: moneyToSave - amount of money to be saved in the file
    try:
        f = open('money.dat', 'w')
        f.write(str(money_to_save))
        f.close()
    except:
        print('Ошибка создания файла, наше Казино закрывается!')
        quit(0)

# ===================================================================================================================


def color(c):  # This function will set color for text showed on the screen
    # Arguments: c - color number
    windll.Kernel32.SetConsoleTextAttribute(h, c)

# ===================================================================================================================


def color_line(c, s):  # This function do colored greeting
    # Arguments: c - color number, s - text to be displayed
    for i in range(30):
        print()
    color(c)
    print('*' * len(s))
    print(' ' + s)
    print('*' * len(s))

# ===================================================================================================================


def win(result):
    color(14)
    print(f'    Победа за тобой! Выигрыш составил {result} {currency}')
    print(f'    У тебя на счету: {money} {currency}')
    print()
    input('    Нажми Enter для продолжения...')

# ===================================================================================================================


def loose(result):
    color(12)
    print(f'    К сожалению ты проиграл {result} {currency}')
    print('    Надо непременно отыграться!')
    print(f'    У тебя на счету: {money} {currency}')
    print()
    input('    Нажми Enter для продолжения...')

# ===================================================================================================================
#  ---- MAIN FUNCTION ----


def main():  # This is main function (METHOD). This function will be launched first
    # From this function we get access to main menu, where we see money amount, can choose game or quit from the game
    # 1. Get money amount from file
    # 2. Main cycle
    #   1. Show greeting message
    #   2. Show menu to choose game
    #   3. Wait for input from user
    #   4. Call for required method or quit from game
    # 3. Show farewell message
    # 4. Show statistics: Win or Lose
    # 5. Write money amount to file
    # 6. Quit from game

    global money, play_game
    money = load_money()  # Load money amount from file
    start_money = money  # Remember start money for statistic at the end

    # ---- Main cycle ---- begin
    while play_game and money > 0:
        # ---- Greetings ---- begin
        color_line(10, 'Приветствую тебя в нашем казино, дружище!')
        color(14)
        print(f'У тебя на счету {money} {currency}')

        color(6)
        print('Ты можешь сыграть в:')
        print('    1. Рулетку')
        print('    2. Кости')
        print('    3. Однорукого бандита')
        print('    0. Выход. Ставка 0 в играх - выход.')
        color(7)
        # ---- Greetings ---- end

        # ---- Ask user for input ---- begin
        x = get_input('0123', '    Твой выбор? ')
        # ---- Ask user for input ---- end

        # ---- Call for required method ---- begin
        if x == '0':
            play_game = False
        elif x == '1':
            roulette()
        elif x == '2':
            dice()
        elif x == '3':
            one_hand_bandit()
        # ---- Call for required method ---- end

    # ---- Main cycle ---- end

    # ---- Farewell message ---- begin
    color_line(12, 'Жаль, что ты покидаешь нас! Но возвращайся скорей!')
    color(13)
    if money <= 0:
        print(' Упс, ты оставлся без денег. Возьми микрокредит и возвращайся!')

    color(11)
    if money > start_money:
        print('Ну что ж, поздравляем с прибылью!')
        print(f'На начало игры у тебя было {start_money} {currency}')
        print(f'Сейчас уже {money} {currency}! Играй ещё и приумножай!')
    elif money == start_money:
        print('Что ж, ты сегодня остался при своих!')
        print('Возвращайся скорее! В следующий раз обязательно выиграешь!')
    else:
        print(f'К сожалению ты проиграл {start_money - money} {currency}')
        print('Надо сыграть ещё, в следующий раз обязательно получится!')
    # ---- Farewell message ---- end

    save_money(money)
    input('    Нажми Enter для выхода')

    color(7)
    quit(0)

# ===================================================================================================================
#  ---- ROULETTE FUNCTIONS ----


def roulette():  # This is main function for Roulette game, it will show menu for roulette
    # 1. Show greeting message and menu
    # 2. Get bid amount and process with bid type
    # 3. Launch animation and get result
    # 4. Show win or lose

    global money
    play_game_roulette = True

    # ---- Main cycle for Roulette ----
    while play_game_roulette and money > 0:

        # 1. Show greeting message and menu
        color_line(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        color(14)
        print(f'\n У тебя на счету {money} {currency}\n')
        color(11)
        print(' Ставлю на...')
        print('    1. Чётное (выигрыш 1:1)')
        print('    2. Нечёное (выигрыш 1:1)')
        print('    3. Дюжина (выигрыш 3:1)')
        print('    4. Число (выигрыш 36:1)')
        print('    0. Возврат в предыдущее меню')

        # 2. Get bid amount and process with bid type
        x = get_input('01234', 'Твой выбор? ')

        play_roulette = True

        if x == '3':
            color(3)
            print()
            print(' Выбери числа:...')
            print('    1. От 1 до 12')
            print('    2. От 12 до 24')
            print('    3. От 24 до 36')
            print('    0. Назад')

            dozen = get_input('0123', 'Твой выбор? ')

            if dozen == '1':
                text_dozen = 'от 1 до 12'
            elif dozen == '2':
                text_dozen = 'от 13 до 24'
            elif dozen == '3':
                text_dozen = 'от 25 до 36'
            elif dozen == '0':
                play_roulette = False

        elif x == '4':
            user_number = get_int_input(0, 36, 'На какое число ставишь? (0..36): ')

        color(7)
        if x == '0':
            return 0

        if play_roulette:
            bid_roulette = get_int_input(0, money, f'Сколько ставишь? (не больше {money} {currency}): ')
            if bid_roulette == 0:
                return 0
            number = get_roulette(visibility)

            print()
            color(11)

            if number < 37:
                print(f'    Выпало число {number}!' + '*' * number)
            else:
                if number == 37:
                    print_number = '00'
                elif number == 38:
                    print_number = '000'
                print(f'    Выпало число {print_number}')

        if x == '1':
            print('    Ты ставил на ЧЁТНОЕ!')
            if (number < 37) and (number % 2 == 0):
                money += bid_roulette
                win(bid_roulette)
            else:
                money -= bid_roulette
                loose(bid_roulette)

        elif x == '2':
            print('    Ты ставил на НЕЧЁТНОЕ!')
            if (number < 37) and (number % 2 != 0):
                money += bid_roulette
                win(bid_roulette)
            else:
                money -= bid_roulette
                loose(bid_roulette)

        elif x == '3':
            print('    Ты ставил на ДЮЖИНУ!')

            win_dozen = ''
            if 1 <= number <= 12:
                win_dozen = '1'
            elif 13 <= number <= 24:
                win_dozen = '2'
            elif 25 <= number <= 36:
                win_dozen = '3'

            if win_dozen == dozen:
                money += bid_roulette * 2
                win(bid_roulette * 3)
            else:
                money -= bid_roulette
                loose(bid_roulette)

        elif x == '4':
            print(f'    Ты ставил на ЧИСЛО {user_number}!')

            if user_number == number:
                money += bid_roulette * 35
                win(bid_roulette * 36)
            else:
                money -= bid_roulette
                loose(bid_roulette)


# -------------------------------------------------------------------------------------------------------------------


def get_roulette(visible):  # This function will show roulette animation and return result
    tick_time = random.randint(100, 200) / 10000
    main_time = 0
    number_roulette = random.randint(0, 38)
    increase_tick_time = random.randint(100, 110) / 100
    col = 1

    while main_time < 0.7:

        col += 1
        if col > 15:
            col = 1

        number_roulette += 1
        if number_roulette > 38:
            number_roulette = 0

        main_time += tick_time
        tick_time *= increase_tick_time

        print_number = number_roulette
        if number_roulette == 37:
            print_number = '00'
        elif number_roulette == 38:
            print_number = '000'

        color(col)
        print('Число', print_number, '*' * number_roulette, ' ' * (79 - number_roulette * 2), '*' * number_roulette)

        if visible:
            time.sleep(main_time)

    return number_roulette

# ===================================================================================================================
# ---- DICE FUNCTIONS ----


def dice():  # This is main function for Dice game, it will show menu for dice
    global money
    play_game_dice = True
    user_bid = 0

    # ---- main dice cycle ----
    while play_game_dice and money > 0:
        color_line(3, 'ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!')
        color(14)

        print(f'\n У тебя на счету {money} {currency}\n')

        user_bid = get_int_input(0, money, f'    Сделай ставку в пределах {money} {currency}: ')
        if user_bid == 0:
            return 0

        control = user_bid  # Variable to keep user bid to debit it if player looses game
        play_round = True  # Flag to keep playing round

        old_result = get_dice()  # Variable for result to compare it with new
        first_play = True  # Flag for first play in round, to draw user bid if he denied to do first bid in round

        # ---- round cycle ----
        while play_round and user_bid > 0:
            if user_bid > money:
                user_bid = money

            color(11)
            print(f'\n    В твоём распоряжении {user_bid} {currency}')
            color(12)
            print(f'\n    Текущая сумма чисел на костях: {old_result}')
            color(11)
            print(f'\n    Сумма чисел на гранях будет больше меньше или равна предыдущей?')
            color(7)
            x = get_input('0123', '    Введи: 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ')

            if x != '0':
                first_play = False

                if user_bid > money:
                    user_bid = money
                money -= user_bid

                new_result = get_dice()

                win_round = False
                if new_result > old_result:
                    if x == '1':
                        win_round = True
                elif new_result < old_result:
                    if x == '2':
                        win_round = True
                if x != '3':
                    if win_round:
                        money += user_bid + user_bid // 5
                        win(user_bid // 5)
                        user_bid += user_bid // 5
                    else:
                        user_bid = control
                        loose(user_bid)
                elif x == '3':
                    if new_result == old_result:
                        money += user_bid + user_bid // 5
                        win(user_bid // 5)
                        user_bid += user_bid // 5
                    else:
                        user_bid = control
                        loose(user_bid)

                old_result = new_result

            else:
                if first_play:
                    money -= user_bid
                    print()
                    print(f'    Передумал? Списываем с твоего счёта {user_bid} {currency}')
                    print()
                    input('    Нажми Enter для прожолжения...')
                play_round = False

# -------------------------------------------------------------------------------------------------------------------


def get_dice():  # This function will show dice animation and return result
    # 1. Decide how many times dices will roll
    # 2. Begin animation cycle and number generation
    # 3. Calculate pause time
    # 4. Return numbers summary
    roll_count = random.randint(3, 8)
    sleep = 0
    while roll_count > 0:
        color(roll_count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(' ' * 10, '----- -----')
        print(' ' * 10, f'| {x} | | {y} |')
        print(' ' * 10, '----- -----')
        time.sleep(sleep)
        sleep += 1 / roll_count
        roll_count -= 1
    result = x + y
    return result

# ===================================================================================================================
# ---- ONE HAND BANDIT FUNCTIONS ----


def one_hand_bandit():  # This is main function for One hand bandit game, it will show menu for One hand bandit game

    global money
    play_one_hand_bandit = True

    while play_one_hand_bandit and money > 0:
        color_line(3, 'ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!')
        color(14)
        print(f'\n У тебя на счету {money} {currency}\n')
        color(5)
        print(' Правила игры: ')
        print('    1. При совпадении 2-х чисел ставка не списывается')
        print('    2. При совпадении 3-х чисел выигрыш 2:1')
        print('    3. При совпадении 4-х чисел выигрыш 5:1')
        print('    4. При совпадении 5-х чисел выигрыш 10:1')
        print('    0. Ставка 0 для завершения игры')

        user_bid = get_int_input(0, money, f'    Введи ставку от 0 до {money}: ')
        if user_bid == 0:
            return 0

        money -= user_bid
        money += one_hand_bandit_res(user_bid)
        if money <= 0:
            play_one_hand_bandit = False

# -------------------------------------------------------------------------------------------------------------------


def one_hand_bandit_res(bid):  # This function receive user bid amount, show animation, calculate and return result

    result = bid

    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    get_d1 = True
    get_d2 = True
    get_d3 = True
    get_d4 = True
    get_d5 = True

    col = 10

    while get_d1 or get_d2 or get_d3 or get_d4 or get_d5:
        if get_d1:
            d1 += 1
            if d1 > 9:
                d1 = 0
            if random.randint(0, 20) == 1:
                get_d1 = False
        if get_d2:
            d2 -= 1
            if d2 < 0:
                d2 = 9
            if random.randint(0, 20) == 1:
                get_d2 = False
        if get_d3:
            d3 += 1
            if d3 > 9:
                d3 = 0
            if random.randint(0, 20) == 1:
                get_d3 = False
        if get_d4:
            d4 -= 1
            if d4 < 0:
                d4 = 9
            if random.randint(0, 20) == 1:
                get_d4 = False
        if get_d5:
            d5 += 1
            if d5 > 9:
                d5 = 0
            if random.randint(0, 20) == 1:
                get_d5 = False

        time.sleep(0.1)
        color(col)
        col += 1
        if col > 15:
            col = 10

        print('    ' + '%' * 10)
        print(f'    {d1} {d2} {d3} {d4} {d5}')

    max_count = get_max_count(d1, d2, d3, d4, d5)

    color(14)
    if max_count == 2:
        print(f' Совпадение двух чисел! Твой выигрыш в размере твоей ставки: {result} {currency}')
        input('    Нажми Enter для продолжения...')
    elif max_count == 3:
        result *= 2
        print(f' Совпадение трёх чисел! Твой выигрыш 2 к 1: {result} {currency}')
        input('    Нажми Enter для продолжения...')
    elif max_count == 4:
        result *= 5
        print(f' Совпадение четырёх чисел! Твой выигрыш 5 к 1: {result} {currency}')
        input('    Нажми Enter для продолжения...')
    elif max_count == 5:
        result *= 10
        print(f' БИНГО! Совпадение Всех чисел! Твой выигрыш 10 к 1: {result} {currency}')
        input('    Нажми Enter для продолжения...')
    else:
        loose(result)
        result = 0

    color(11)
    print()

    return result

# -------------------------------------------------------------------------------------------------------------------


def get_max_count(v1, v2, v3, v4, v5):  # This function counts digits in result
    control = 0
    for j in (v1, v2, v3, v4, v5):
        count = 0
        for i in (v1, v2, v3, v4, v5):
            if j == i:
                count += 1
        if count > control:
            control = count
    return count

# ===================================================================================================================


main()
