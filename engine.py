import tdl
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width /2), int(screen_height / 2), '@', (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', (255, 255, 0))
    entities = [npc, player]

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tdl.set_font('arial12x12.png', greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height, title='Roguelike Tutorial Revised', \
                            renderer='GLSL')
    con = tdl.Console(screen_width, screen_height)

    while not tdl.event.is_window_closed():
        render_all(con, entities, root_console, screen_width, screen_height)
        tdl.flush()

        clear_all(con, entities)


        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
        else:
            user_input = None

        if not user_input:
            continue

        action = handle_keys(user_input)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        screenshot = action.get('screenshot')

        if move:
            dx, dy = move
            player.move(dx, dy)
        if screenshot:
            print('taking screenshot?')
            tdl.screenshot()

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

if __name__ == '__main__':
    main()