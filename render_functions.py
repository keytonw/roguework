def render_all(con, entities, root_console, screen_width, screen_height):
    # Draw all entities on the screen.
    for entity in entities:
        draw_entity(con, entity)

    root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    con.draw_char(entity.x, entity.y, entity.char, entity.color, bg = None)


def clear_entity(con, entity):
    # Erase the character that represents this object.
    con.draw_char(entity.x, entity.y, ' ', bg=None)