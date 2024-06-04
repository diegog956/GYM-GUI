import customtkinter as ctk
from . import Left_Admin_Frame


class Right_Admin_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame, controller):
        super().__init__(app, border_width=2, border_color='#2CC985')

        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, text='boton', command=self.controller.change)
        self.button.grid(row=0, column=0)

    def funciones(self):

    # Lo relevante en terminos de cambio de right admin frame va aca,
    # y luego se llama desde el Admin_Frame en una funcion homnima

        pass
