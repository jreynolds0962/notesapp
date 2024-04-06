from flet import TextField, Container, TextStyle, FontWeight, colors, padding

title_txtfield = TextField(
    text_style=TextStyle(font_family="Arial", size=24, weight=FontWeight.BOLD),
    border="none",
    autofocus=True,
    hint_text="Title",
    cursor_color="purple",
    selection_color=colors.PURPLE_400
)

title = Container(
    content=title_txtfield,
    padding=padding.only(left=40, top=10)
)