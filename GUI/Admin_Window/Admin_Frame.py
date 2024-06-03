import customtkinter as ctk
import pywinstyles
from PIL import Image


class Admin_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame):
        super().__init__(app, fg_color='#343434')
        self.app = app

        # Rows
        self.grid_rowconfigure(0, weight=1)

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)


        menu_frame = ctk.CTkFrame(self, border_width=2,border_color='white')
        menu_frame.grid(row=0, column=0, sticky='nsew')

        main_frame=ctk.CTkFrame(self, border_width=2,border_color='white')
        main_frame.grid(row=0, column=1, sticky='nsew')

