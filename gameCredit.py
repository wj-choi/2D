from pico2d import *
import framework
import gameCopyright
import game
import level_3

name = "credit"
background = None
kpu = None
logo_time = 0
opacify = 1
bgm = None


def enter():
    global bgm
    open_canvas(1000, 500, sync=True)
    framework.push_state(level_3)
    global background, kpu
    background = load_image("back.png")
    kpu = load_image("kpu.png")
    bgm = load_music('alone.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                framework.push_state(gameCopyright)


def update(frame_time):
    global opacify, logo_time

    logo_time += 1
    game.move -= 1

    if logo_time > 100:
        opacify -= 0.02

    if opacify < 0:
        framework.push_state(gameCopyright)


def draw(frame_time):
    clear_canvas()
    for i in range(10):
        for j in range(10):
            background.draw(game.background_x + 1000 * i + game.move, game.background_y + 500 * j + game.move)

    kpu.draw(505, 260)
    kpu.opacify(opacify)
    update_canvas()



