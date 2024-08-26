import flet as ft

def main(page: ft.Page):
    page.title = "AI Psychologist"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    token = ft.TextField(label="Prompt", icon="chat")

    def send_prompt(e):

    page.add(
        ft.Row(
            [
                token,
                ft.FilledButton("Send prompt", icon="send", on_click=send_prompt)

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)