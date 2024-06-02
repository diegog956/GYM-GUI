from GUI.Access_Window.Image_Frame import *
import tkinter as tk

# Bloque que permite centrar la app al abrir
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 700
x_pos = (screen_width - width) // 2
y_pos = (screen_height - height) // 2
root.destroy()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set size and the initial position of the window
        self.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

        # Set Title
        self.title("GYM")

        # Make it resizable
        self.resizable()

        # Set the Grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Assign the logo
        self.iconbitmap(r'logo_gym.ico')

        # Create the ImageFrame and place it over the grid
        self.image_frame = Image_Frame(self)
        self.image_frame.grid(row=0, column=0, sticky='nsew')
