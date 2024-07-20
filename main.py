import badger2040
from pngdec import PNG
import time

badger = badger2040.Badger2040()
png = PNG(badger.display)


def fill(color=15):
    badger.set_pen(color)
    badger.clear()


def update(speed=2):
    badger.set_update_speed(speed)
    badger.update()

makespace_last_updated = time.time()

def makespace_png():
    global makespace_last_updated
    delta = time.time() - makespace_last_updated
    if prev_program == program_idx and delta >= 10:
        print('off')
        badger2040.turn_off()
        return
    if prev_program == program_idx:
        return
    fill()
    png.open_file("makespace.png")
    png.decode(0, 0)
    update(1)
    makespace_last_updated = time.time()

daniel_png_last_updated = time.time()

def daniel_png():
    global daniel_png_last_updated
    delta = time.time() - daniel_png_last_updated
    if prev_program == program_idx and delta >= 10:
        print('off')
        badger2040.turn_off()
        return
    if prev_program == program_idx:
        return
    fill()
    png.open_file("daniel.png")
    png.decode(0, 0)
    update(1)
    daniel_png_last_updated = time.time()


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


topics = [
    "event sourcing\nand CQRS",
    "ergonomic\nkeyboards",
    "full time\nensembling",
    "choosing what\nto implement",
    "GitOps\n(without k8s)",
    "TDD & CI/CD\non hardware",
]

last_lets_talk_update = 0
current_topic = 0


def lets_talk():
    RATE = 60
    global last_lets_talk_update
    global current_topic
    time_delta = time.time() - last_lets_talk_update
    if not time_delta > RATE and prev_program == program_idx:
        return
    last_lets_talk_update = time.time()

    fill(15)
    badger.set_pen(0)

    badger.set_font("bitmap14_outline")
    badger.text("let's talk", 0, 0)
    badger.set_font("bitmap8")
    badger.text(topics[current_topic], 0, 32, scale=4)
    current_topic = (current_topic + 1) % len(topics)
    update(2)


programs = [
    makespace_png,
    daniel_png,
    lets_talk,
]


program_idx = 2
prev_program = 0
programs[program_idx - 1]()

while True:
    prev_program = program_idx
    program_count = len(programs)
    if badger.pressed(badger2040.BUTTON_UP):
        program_idx = clamp(program_idx + 1, 1, program_count)
    if badger.pressed(badger2040.BUTTON_DOWN):
        program_idx = clamp(program_idx - 1, 1, program_count)
    if prev_program != program_idx:
        print(f"Running program {program_idx}")
    programs[program_idx - 1]()
