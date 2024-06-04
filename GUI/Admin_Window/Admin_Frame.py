import customtkinter as ctk

from GUI.Admin_Window.Left_Admin_Frame import Left_Admin_Frame
from GUI.Admin_Window.Right_Admin_Frame import Right_Admin_Frame


class Admin_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame, back_main_frame):
        super().__init__(app, fg_color='#343434')
        self.back_main_frame = back_main_frame
        self.app = app

        # Rows
        self.grid_rowconfigure(0, weight=1)

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        # Menu Frame - Left
        self.menu_frame = Left_Admin_Frame(self, self.back_main_frame)
        self.menu_frame.grid(row=0, column=0, sticky='nsew')

        # Main Frame - Right
        self.main_frame = Right_Admin_Frame(self, self)
        self.main_frame.grid(row=0, column=1, sticky='nsew')

    def change(self):
        pass