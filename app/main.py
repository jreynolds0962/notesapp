from flet import *
from Title import title, title_txtfield
from Text import text, textfield

def main(page: Page):
    page.title = "Notesapp"
    page.scroll = True
    page.theme_mode = ThemeMode.DARK
    
    def changetheme(e):
        page.theme_mode = (
            ThemeMode.LIGHT
            if page.theme_mode == ThemeMode.DARK
            else ThemeMode.DARK
        )
        
        toggleButton.selected = not toggleButton.selected
        
        page.update()
        
    toggleButton = IconButton(on_click=changetheme,
                              icon="nightlight",
                              selected_icon="light_mode_outlined",
                              style=ButtonStyle(color={"":colors.WHITE, "selected":colors.BLACK}),)
    
    
    def save_text(e: ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(f"{title_txtfield.value}\n{textfield.value}")
    
    def load_text(e: ControlEvent):
        try:
            with open('save.txt', 'r') as f:
                lines = f.readlines()
                if lines:
                    title_text = lines[0].strip()
                    title_txtfield.value = title_text
                    textfield.value = ''.join(lines[1:])
                else:
                    title_txtfield.value = ''
        except FileNotFoundError:
            textfield.hint_text = "Welcome to the notes app!"
    
    title_txtfield.on_change, textfield.on_change = save_text, save_text
    load_text(None)

    page.add(
        title,
        text,
        AppBar(
            leading=Icon(icons.TEXT_SNIPPET),
            title=Text("Notes app"),
            actions=[toggleButton],
            bgcolor=colors.SURFACE_VARIANT
        )
    )

app(target=main)