def handle_keys(user_input):
    key_char = user_input.char

    # Movement keys
    if user_input.key == 'UP' or key_char == 'i':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN' or key_char == ',':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT' or key_char == 'j':
        return {'move': (-1,0)}
    elif user_input.key == 'RIGHT' or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'u':
        return {'move': (-1, -1)}
    elif key_char == 'o':
        return {'move': (-1, 1)}
    elif key_char == 'm':
        return {'move': (-1, 1)}
    elif key_char == '.':
        return {'move': (1, 1)}

    if user_input.key == 'ENTER' and user_input.alt:
        #ALT+ENTER: toggles full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        return {'exit': True}
    elif user_input.key == 'TAB':
        #ALT+F12: takes a screenshot
        return {'screenshot': True}

    # If no key was pressed...
    return {}