import badger2040
from pngdec import PNG

badger = badger2040.Badger2040()
png = PNG(badger.display)


def white():
    badger.set_pen(15)
    badger.clear()


def update(speed=2):
    badger.set_update_speed(speed)
    badger.update()


def daniel_png():
    if prev_program == program:
        return
    white()
    png.open_file("daniel.png")
    png.decode(0, 0)
    update()


def daniel_txt():
    if prev_program == program:
        return
    white()
    badger.set_pen(0)
    badger.set_thickness(7)
    badger.set_font("serif")
    badger.text("daniel", 20, 80, scale=2.5)
    badger.set_font("sans")
    badger.set_thickness(2)
    badger.text("he/him", 20, 20, scale=0.8)
    update()


programs = [
    daniel_png,
    daniel_txt,
]
prev_program = 2
program = 1
program_count = len(programs)


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


while True:
    prev_program = program
    if badger.pressed(badger2040.BUTTON_UP):
        program = clamp(program + 1, 1, program_count)
    if badger.pressed(badger2040.BUTTON_DOWN):
        program = clamp(program - 1, 1, program_count)
    if prev_program != program:
        print(program)
    programs[program - 1]()
