def handle_keys(user_input):
    # Movement keys
    if user_input.key == 'UP':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT':
        return {'move': (-1,0)}
    elif user_input.key == 'RIGHT':
        return {'move': (1,0)}

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