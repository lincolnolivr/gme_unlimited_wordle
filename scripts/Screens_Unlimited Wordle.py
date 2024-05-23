from tracemalloc import start
import flet as ft

def main(page: ft.Page):

    def home_page(e=None):
        page.controls.clear()
        # Page settings
        page.title = "Unlimited Wordle"
        page.window_width = 800
        page.window_height = 600
        page.window_resizable = False
        page.padding = 100
        page.theme_mode = 'dark'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        def button_click(e):
            navigate_to("/start_page")

        text = ft.Text("Unlimited Wordle", size=24, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.RIGHT)
        name_input = ft.TextField(label="Name", autofocus=True, hint_text="Enter your name")
        submit_button = ft.ElevatedButton(text="Submit", on_click=button_click, expand=2)
        row = ft.Row(controls=[submit_button], spacing=10)
        page.update()
        page.add(text, name_input, row)

    def start_page(e=None):
        page.controls.clear()
        # Page settings
        page.title = "Page 1"
        page.window_width = 800
        page.window_height = 600
        page.window_resizable = False
        page.padding = 100
        page.theme_mode = 'dark'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        def button_click(e):
            navigate_to("/start_game")

        text = ft.Text(f"Bem vindo, ", size=24, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.RIGHT)
        start_button = ft.ElevatedButton(text="Start", on_click=button_click, expand=2)
        settings_button = ft.ElevatedButton(text="Settings", on_click=button_click, expand=2)
        

        row_1 = ft.Row(controls=[start_button], spacing=10)
        row_2 = ft.Row(controls=[settings_button], spacing=10)

        page.update()
        page.add(text, row_1, row_2)
    

    # Função para navegar para uma rota específica
    def navigate_to(route):
        if route == "/":
            home_page()
        elif route == "/start_page":
            start_page()
        elif route == "/start_game":
            ...
            #page2()
        page.update()

    # Configura o roteamento
    page.on_route_change = lambda e: navigate_to(e.route)
    # Define a rota inicial
    navigate_to(page.route)
    #page.update()

ft.app(target=main)