from .terminal_width_ui import terminal_width

def center_text(text):
    return text.center(terminal_width())