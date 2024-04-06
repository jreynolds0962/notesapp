from flet import TextField, Container, TextStyle, colors, padding

textfield = TextField(
    text_style=TextStyle(font_family="Arial", size=18),
    multiline=True,
    border="none",
    min_lines=40,
    cursor_color="purple",
    selection_color=colors.PURPLE_400
)

text = Container(
    content=textfield,
    padding=padding.only(left=40)
)