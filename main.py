import tkinter as tk
from GUI.app import App
from db.db import *
import customtkinter as ctk


# connection = create_connection()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


app = App()

app.mainloop()
#connection.close()

