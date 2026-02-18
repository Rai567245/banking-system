from .terminal_width_ui import terminal_width

def banner(char="=", margin=200):
    width = terminal_width() - margin
    return char * max(width, 10)