WIDTH, LENGTH = 600, 700
ROWS = 40

COLORS = {
    "GREEN": (0, 200, 0),
    "GREY": (128, 128, 128),
    "BLACK": (0, 0, 0),
}

MENU_POS = (0, WIDTH)
MENU_SIZE = (WIDTH, LENGTH - WIDTH)

BTN_SIZE = (120, 50)

MENU_BTNS = (
    (
        "main",
        (
            ("start", "Start node"),
            ("end", "End node"),
            ("wall", "Build wall"),
            ("find", "Find path"),
        ),
    ),
    ("end", (("reset", "Reset"),)),
)
