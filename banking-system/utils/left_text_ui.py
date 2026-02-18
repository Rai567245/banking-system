from .terminal_width_ui import terminal_width

def left_text(text, offset=10):
    centered = text.center(terminal_width())
    return centered[offset:]