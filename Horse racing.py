# ===================
# ==== LIBRARIES ====
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ===============================
# ==== METHODS AND FUNCTIONS ====
# ===========================
# ==== SERVICE FUNCTIONS ====


def horse_place_in_window():  # To draw horse at the screen
    horse_01.place(x=int(x01), y=20)
    horse_02.place(x=int(x02), y=100)
    horse_03.place(x=int(x03), y=180)
    horse_04.place(x=int(x04), y=260)


def load_money():  # To load money amount from file
    try:
        f = open('horse_money.dat', 'r')
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f'Файла не существует, задано значение {default_money} {currency}')
        m = default_money
    return m


def save_money(money_to_save):  # To save money to file
    try:
        f = open('horse_money.dat', 'w')
        f.write(str(money_to_save))
        f.close()
    except:
        print('Ошибка создания файла, наш Ипподром закрывается!')
        quit(0)


def refresh_combo(event_object):  # To update bids list, if money amount is changed (bid on another horse is done)
    summ = bid_01_summ.get() + bid_02_summ.get() + bid_03_summ.get() + bid_04_summ.get()
    label_all_money['text'] = f'У вас на счету осталось {int(money - summ)} {currency}'

    bid_01['values'] = get_values(
        int(money - bid_01_summ.get() - bid_02_summ.get() - bid_03_summ.get() - bid_04_summ.get()))
    bid_02['values'] = get_values(
        int(money - bid_01_summ.get() - bid_02_summ.get() - bid_03_summ.get() - bid_04_summ.get()))
    bid_03['values'] = get_values(
        int(money - bid_01_summ.get() - bid_02_summ.get() - bid_03_summ.get() - bid_04_summ.get()))
    bid_04['values'] = get_values(
        int(money - bid_01_summ.get() - bid_02_summ.get() - bid_03_summ.get() - bid_04_summ.get()))

    if summ > 0:
        start_button['state'] = 'normal'
    elif summ <= 0:
        start_button['state'] = 'disabled'

    if bid_01_summ.get() > 0:
        horse_01_game.set(True)
    else:
        horse_01_game.set(False)

    if bid_02_summ.get() > 0:
        horse_02_game.set(True)
    else:
        horse_02_game.set(False)

    if bid_03_summ.get():
        horse_03_game.set(True)
    else:
        horse_03_game.set(False)

    if bid_04_summ.get() > 0:
        horse_04_game.set(True)
    else:
        horse_04_game.set(False)


def get_values(mny):  # To calculate bids list
    values = []
    if money > 9:
        step = mny // 10
        bid = 0
        values.append(0)
        for i in range(10):
            bid += step
            values.append(bid)
        return values
    else:
        values.append(0)
        if mny > 0:
            values.append(mny)


def win_round(horse):
    global x01, x02, x03, x04, money
    result = 'К финишу пришла лошадь '
    win = 0
    if horse == 1:
        result += horse_01_name
        win = bid_01_summ.get() * win_coef_01
    elif horse == 2:
        result += horse_02_name
        win = bid_02_summ.get() * win_coef_02
    elif horse == 3:
        result += horse_03_name
        win = bid_03_summ.get() * win_coef_03
    elif horse == 4:
        result += horse_04_name
        win = bid_04_summ.get() * win_coef_04

    if horse > 0:
        result += f'! Вы выиграли {int(win)} {currency}'
        if win > 0:
            result += '! Поздравляем! Средства уже зачислены на ваш счёт!'
        else:
            result += '! К сожалению, ваша лошадь была неправильной. Попробуйте ещё раз!'
            insert_text('Делайте ставку! Увеличивайте прибыль!')
        messagebox.showinfo('РЕЗУЛЬТАТ', result)
    else:
        messagebox.showinfo('Всё плохо', 'До финиша не дошёл никто. Забег признан несостоявшимся. Все ставки возвращены.')
        insert_text('Забег признан несостоявшимся.')
        win = bid_01_summ.get() + bid_02_summ.get() + bid_03_summ.get() + bid_04_summ.get()

    money += win
    save_money(int(money))

    start_button['state'] = 'normal'

    bid_01['state'] = 'readonly'
    bid_02['state'] = 'readonly'
    bid_03['state'] = 'readonly'
    bid_04['state'] = 'readonly'

    bid_01.current(0)
    bid_02.current(0)
    bid_03.current(0)
    bid_04.current(0)

    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20

    horse_place_in_window()

    refresh_combo('')
    view_weather()
    view_horse_health()
    insert_text(f'Ваши средства; {int(money)} {currency}')

    if money < 1:
        messagebox.showinfo('Стоп!', 'Здесь без денег делать нечего!')
        quit(0)


def setup_horse():
    global state_01, state_02, state_03, state_04, weather, time_day
    global win_coef_01, win_coef_02, win_coef_03, win_coef_04, fast_speed_01, fast_speed_02, fast_speed_03, fast_speed_04
    global play_01, play_02, play_03, play_04, reverse_01, reverse_02, reverse_03, reverse_04

    weather = random.randint(1, 4)
    time_day = random.randint(1, 4)

    state_01 = random.randint(1, 5)
    state_02 = random.randint(1, 5)
    state_03 = random.randint(1, 5)
    state_04 = random.randint(1, 5)

    win_coef_01 = int(100 + random.randint(1, 30 + state_01 * 60)) / 100
    win_coef_02 = int(100 + random.randint(1, 30 + state_02 * 60)) / 100
    win_coef_03 = int(100 + random.randint(1, 30 + state_03 * 60)) / 100
    win_coef_04 = int(100 + random.randint(1, 30 + state_04 * 60)) / 100

    reverse_01 = False
    reverse_02 = False
    reverse_03 = False
    reverse_04 = False

    play_01 = True
    play_02 = True
    play_03 = True
    play_04 = True

    fast_speed_01 = False
    fast_speed_02 = False
    fast_speed_03 = False
    fast_speed_04 = False

# ========================
# ==== INFO FUNCTIONS ====


def insert_text(s):  # To add message to info-chat
    info_chat.insert(INSERT, s + '\n')
    info_chat.see(END)


def view_weather():  # To add weather status message to info-chat
    s = 'Сейчас на ипподроме '
    if time_day == 1:
        s += 'ночь, '
    elif time_day == 2:
        s += 'утро, '
    elif time_day == 3:
        s += 'вечер, '
    elif time_day == 4:
        s += 'ночь, '

    if weather == 1:
        s += 'льёт сильный дожди.'
    elif weather == 2:
        s += 'моросит дождик.'
    elif weather == 3:
        s += 'облачно, на горизонте тучи.'
    elif weather == 4:
        s += 'безоблачно, прекрасная погода!'

    insert_text(s)


def view_horse_health():  # To add horse condition message at info chat
    insert_text(health_horse(horse_01_name, state_01, win_coef_01))
    insert_text(health_horse(horse_02_name, state_02, win_coef_02))
    insert_text(health_horse(horse_03_name, state_03, win_coef_03))
    insert_text(health_horse(horse_04_name, state_04, win_coef_04))

# ============================
# ==== GAMEPLAY FUNCTIONS ====


def move_horse():  # To calculate horses position and move them
    global x01, x02, x03, x04

    if random.randint(1, 100) < 20:
        problem_horse()

    speed_01 = (random.randint(1, time_day + weather) + random.randint(1, int((7 - state_01)) * 3)) / random.randint(10, 175)  # Setup speed
    speed_02 = (random.randint(1, time_day + weather) + random.randint(1, int((7 - state_02)) * 3)) / random.randint(10, 175)
    speed_03 = (random.randint(1, time_day + weather) + random.randint(1, int((7 - state_03)) * 3)) / random.randint(10, 175)
    speed_04 = (random.randint(1, time_day + weather) + random.randint(1, int((7 - state_04)) * 3)) / random.randint(10, 175)

    multiple = 2

    speed_01 *= random.randint(1, 2 + state_01) * (1 + fast_speed_01 * multiple)
    speed_02 *= random.randint(1, 2 + state_02) * (1 + fast_speed_01 * multiple)
    speed_03 *= random.randint(1, 2 + state_03) * (1 + fast_speed_01 * multiple)
    speed_04 *= random.randint(1, 2 + state_04) * (1 + fast_speed_01 * multiple)

    if play_01:
        if reverse_01:
            x01 -= speed_01
        else:
            x01 += speed_01

    if play_02:
        if reverse_02:
            x02 -= speed_02
        else:
            x02 += speed_02

    if play_03:
        if reverse_03:
            x03 -= speed_03
        else:
            x03 += speed_03

    if play_04:
        if reverse_04:
            x04 -= speed_04
        else:
            x04 += speed_04

    all_play = play_01 or play_02 or play_03 or play_04  # Flag will be True if all horses will not move
    all_x = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0  # Flag will be True if all horses will run away to the left
    all_reverse = reverse_01 and reverse_02 and reverse_03 and reverse_04  # Flag will be True if all horses run to the left

    if not all_play or all_x or all_reverse:
        win_round(0)
        return 0

    horse_place_in_window()

    if x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952:  # If run not ended
        root.after(5, move_horse)  # Repeat after 5 mSec.
    else:
        if x01 >= 952:
            win_round(1)
        if x02 >= 952:
            win_round(2)
        if x03 >= 952:
            win_round(3)
        if x04 >= 952:
            win_round(4)


def run_horse():  # To block bids and run "def move_horse():"
    global money
    start_button['state'] = 'disabled'
    bid_01['state'] = 'disabled'
    bid_02['state'] = 'disabled'
    bid_03['state'] = 'disabled'
    bid_04['state'] = 'disabled'
    money -= bid_01_summ.get() + bid_02_summ.get() + bid_03_summ.get() + bid_04_summ.get()
    move_horse()


def problem_horse():  # To generate emergency situation
    global reverse_01, reverse_02, reverse_03, reverse_04
    global play_01, play_02, play_03, play_04
    global fast_speed_01, fast_speed_02, fast_speed_03, fast_speed_03

    horse = random.randint(1, 4)
    # The higher the number, the lower the problem chance
    max_rand = 10000

    if horse == 1 and play_01 and x01 > 0:
        if random.randint(0, max_rand) < 5 - state_01:
            reverse_01 = not reverse_01
            messagebox.showinfo('Аааааа!', f'Лошадь {horse_01_name} развернулась и бежит в другую сторону!')
        elif random.randint(0, max_rand) < 5 - state_01:
            play_01 = False
            messagebox.showinfo('Никогда такого не было и вот опять', f'{horse_01_name} заржала и скинула жокея!')
        elif random.randint(0, max_rand) < 5 - state_01:
            fast_speed_01 = True
            messagebox.showinfo('Великолепно!', f'{horse_01_name} перестала притворяться и ускорилась!')

    elif horse == 2 and play_02 and x02 > 0:
        if random.randint(0, max_rand) < 5 - state_02:
            reverse_02 = not reverse_02
            messagebox.showinfo('Аааааа!', f'Лошадь {horse_02_name} развернулась и бежит в другую сторону!')
        elif random.randint(0, max_rand) < 5 - state_02:
            play_02 = False
            messagebox.showinfo('Никогда такого не было и вот опять', f'{horse_02_name} заржала и скинула жокея!')
        elif random.randint(0, max_rand) < 5 - state_02:
            fast_speed_02 = True
            messagebox.showinfo('Великолепно!', f'{horse_02_name} перестала притворяться и ускорилась!')

    elif horse == 3 and play_03 and x03 > 0:
        if random.randint(0, max_rand) < 5 - state_03:
            reverse_03 = not reverse_03
            messagebox.showinfo('Аааааа!', f'Лошадь {horse_03_name} развернулась и бежит в другую сторону!')
        elif random.randint(0, max_rand) < 5 - state_03:
            play_03 = False
            messagebox.showinfo('Никогда такого не было и вот опять', f'{horse_03_name} заржала и скинула жокея!')
        elif random.randint(0, max_rand) < 5 - state_03:
            fast_speed_03 = True
            messagebox.showinfo('Великолепно!', f'{horse_03_name} перестала притворяться и ускорилась!')

    elif horse == 4 and play_04 and x04 > 0:
        if random.randint(0, max_rand) < 5 - state_04:
            reverse_04 = not reverse_04
            messagebox.showinfo('Аааааа!', f'Лошадь {horse_04_name} развернулась и бежит в другую сторону!')
        elif random.randint(0, max_rand) < 5 - state_04:
            play_04 = False
            messagebox.showinfo('Никогда такого не было и вот опять', f'{horse_04_name} заржала и скинула жокея!')
        elif random.randint(0, max_rand) < 5 - state_04:
            fast_speed_04 = True
            messagebox.showinfo('Великолепно!', f'{horse_04_name} перестала притворяться и ускорилась!')


def health_horse(name, state, win):  # To setup horse condition
    s = f'Лошадь {name} '
    if state == 5:
        s += 'мучается несварением желудка.'
    elif state == 4:
        s += 'плохо спала. Подёргивается веко.'
    elif state == 3:
        s += 'сурова и беспощадна.'
    elif state == 2:
        s += 'в отличном настроении, покушала хорошо. '
    elif state == 1:
        s += 'просто ракета!'

    s += f' ({win}:1)'
    return s

root = Tk()

# ===================
# ==== Variables ====

# Program window size
WIDTH = 1024
HEIGHT = 600

# Start "x" coordinates for horses
x01 = x02 = x03 = x04 = 20  # Setup "x" coordinate for all horses

# Horses names
horse_01_name = 'Идальго'
horse_02_name = 'Буцефал'
horse_03_name = 'Росинант'
horse_04_name = 'Конёк-Горбунок'

# ---- Situation flags ----
reverse_01 = False
reverse_02 = False
reverse_03 = False
reverse_04 = False

play_01 = True
play_02 = True
play_03 = True
play_04 = True

fast_speed_01 = False
fast_speed_02 = False
fast_speed_03 = False
fast_speed_04 = False

# Money
money = 0
default_money = 10000
currency = 'руб.'

# ===================
# ==== INTERFACE ====

# ---- Creating window ----
# Calculating coordinates
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
# Setup window name
root.title('ИППОДРОМ')
# Restrict window resize
root.resizable(False, False)
# Setup coordinates and window size
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# ---- Road -----
road_image = PhotoImage(file='road.png')  # Load image
road = Label(root, image=road_image)  # Create widget for road and assign image (Example of Label)
road.place(x=0, y=17)  # Show widget

# ---- Horses ----
horse_01_image = PhotoImage(file='horse01.png')  # Load image
horse_01 = Label(root, image=horse_01_image)  # Create widget for horse and assign image (Example of Label)

horse_02_image = PhotoImage(file='horse02.png')
horse_02 = Label(root, image=horse_02_image)

horse_03_image = PhotoImage(file='horse03.png')
horse_03 = Label(root, image=horse_03_image)

horse_04_image = PhotoImage(file='horse04.png')
horse_04 = Label(root, image=horse_04_image)

horse_place_in_window()

# ---- Button START ----
start_button = Button(text='СТАРТ', font='arial 20', width=61, background='#37AA37')  # Create widget for start button (Example of Button)
start_button.place(x=20, y=370)  # Show widget

# ---- Info chat ----
info_chat = Text(width=70, height=8, wrap=WORD)  # Create widget for Information chat (Example of Text)
info_chat.place(x=430, y=450)  # Show widget

scroll = Scrollbar(command=info_chat.yview, width=20)  # Create widget for Scrollbar (Example of Scrollbar)
scroll.place(x=990, y=450, height=132)  # Show widget

info_chat['yscrollcommand'] = scroll.set

# ---- Money amount ----
money = load_money()  # Load money amount from file

if money < 1:  # If zero money, playing game is forbidden
    messagebox.showinfo('Стоп!', 'Здесь без денег делать нечего!')
    quit(0)

label_all_money = Label(text=f'Осталось средств: {int(money)} {currency}')  # Create widget for money (Example of Label)
label_all_money.place(x=20, y=565)  # Show widget

# ---- Weather ----
weather = random.randint(1, 5)  # 1 - bad weather ... 5 - good weather

# ---- Time of the day
time_day = random.randint(1, 4)  # 1 - night, 2 - morning, 3 - day, 4 - evening

# ---- Bids ----
label_horse_01 = Label(text='Ставка на лошадь №1')  # Create widget for bid name (Example of Label)
label_horse_01.place(x=20, y=450)  # Show widget

label_horse_02 = Label(text='Ставка на лошадь №2')
label_horse_02.place(x=20, y=480)

label_horse_03 = Label(text='Ставка на лошадь №3')
label_horse_03.place(x=20, y=510)

label_horse_04 = Label(text='Ставка на лошадь №4')
label_horse_04.place(x=20, y=540)

# ---- Checkbox ----
horse_01_game = BooleanVar()  # Create variable for checkbox
horse_01_game.set(0)
horse_01_check = Checkbutton(text=horse_01_name, variable=horse_01_game, onvalue=1, offvalue=0)  # Create widget for checkbox
horse_01_check.place(x=150, y=448)  # Show widget

horse_02_game = BooleanVar()
horse_02_game.set(0)
horse_02_check = Checkbutton(text=horse_02_name, variable=horse_02_game, onvalue=1, offvalue=0)
horse_02_check.place(x=150, y=478)

horse_03_game = BooleanVar()
horse_03_game.set(0)
horse_03_check = Checkbutton(text=horse_03_name, variable=horse_03_game, onvalue=1, offvalue=0)
horse_03_check.place(x=150, y=508)

horse_04_game = BooleanVar()
horse_04_game.set(0)
horse_04_check = Checkbutton(text=horse_04_name, variable=horse_04_game, onvalue=1, offvalue=0)
horse_04_check.place(x=150, y=538)

horse_01_check['state'] = 'disabled'
horse_02_check['state'] = 'disabled'
horse_03_check['state'] = 'disabled'
horse_04_check['state'] = 'disabled'

# ---- Dropdown menu ----
bid_01 = ttk.Combobox(root)  # Create widget for dropdown menu (Example of Combobox)
bid_02 = ttk.Combobox(root)
bid_03 = ttk.Combobox(root)
bid_04 = ttk.Combobox(root)

bid_01['state'] = 'readonly'
bid_01.place(x=280, y=450)  # Show widget

bid_02['state'] = 'readonly'
bid_02.place(x=280, y=480)

bid_03['state'] = 'readonly'
bid_03.place(x=280, y=510)

bid_04['state'] = 'readonly'
bid_04.place(x=280, y=540)

# ---- Variables for bid ----
bid_01_summ = IntVar()  # Variable to keep bid amount
bid_02_summ = IntVar()
bid_03_summ = IntVar()
bid_04_summ = IntVar()

bid_01['textvariable'] = bid_01_summ
bid_02['textvariable'] = bid_02_summ
bid_03['textvariable'] = bid_03_summ
bid_04['textvariable'] = bid_04_summ

bid_01.bind('<<ComboboxSelected>>', refresh_combo)
bid_02.bind('<<ComboboxSelected>>', refresh_combo)
bid_03.bind('<<ComboboxSelected>>', refresh_combo)
bid_04.bind('<<ComboboxSelected>>', refresh_combo)

refresh_combo('')

bid_01.current(0)
bid_02.current(0)
bid_03.current(0)
bid_04.current(0)

# ---- Horse health ----
state_01 = random.randint(1, 4)
state_02 = random.randint(1, 4)
state_03 = random.randint(1, 4)
state_04 = random.randint(1, 4)

# ---- Win coefficients ----
win_coef_01 = int(100 + random.randint(1, 30 + state_01 * 60)) / 100
win_coef_02 = int(100 + random.randint(1, 30 + state_02 * 60)) / 100
win_coef_03 = int(100 + random.randint(1, 30 + state_03 * 60)) / 100
win_coef_04 = int(100 + random.randint(1, 30 + state_04 * 60)) / 100


view_weather()
view_horse_health()

start_button['command'] = run_horse

root.mainloop()
