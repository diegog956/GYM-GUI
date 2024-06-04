import customtkinter as ctk
import pywinstyles
from PIL import Image
from GUI.Access_Window.Central_Frame import Central_Frame
from GUI.Admin_Window.Admin_Frame import Admin_Frame


class Image_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTk):
        super().__init__(app)
        self.admin_frame = None
        self.central_frame = None
        self.app = app
        # Grid Configuration
        # Row/s
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)

        # Columns
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=5)

        # Background Image
        self.image = ctk.CTkImage(dark_image=Image.open('GUI/Access_Window/assets/background-image.jpg'))
        self.aux_label = ctk.CTkLabel(self, image=self.image, text='')
        self.aux_label.grid(row=0, column=0, columnspan=3, rowspan=3, sticky='nswe')

        # Central Frame
        self.central_frame = Central_Frame(self, self.app, self.show_admin_frame)
        self.central_frame.grid(row=0, column=1, rowspan=3, sticky='nsew')

        # Bind the dimension changes resizing the frame
        self.bind("<Configure>", self.bg_image_resizer)

        # Store the original image for resizing purposes
        self.original_image = Image.open(r'GUI/Access_Window/assets/background-image.jpg')

    def bg_image_resizer(self, event) -> None:
        # Opens the images setting the width and height of the app with the window one and put it on the same label
        i = ctk.CTkImage(dark_image=self.original_image, size=(self.winfo_width(), self.winfo_height()))
        self.aux_label.configure(text="", image=i)

    # def create_image_frame(self):
    #     self.central_frame = Central_Frame(self, self.app)
    #     self.central_frame.grid(row=0, column=1, rowspan=3, sticky='nsew')

    def show_admin_frame(self):
        self.central_frame.destroy()

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=1)

        self.admin_frame = Admin_Frame(self, self.back_main_frame)
        pywinstyles.set_opacity(self.admin_frame, 0.97)
        self.admin_frame.grid(column=1, row=1, sticky='nsew')

    def back_main_frame(self):
        self.admin_frame.destroy()

        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)

        # Columns
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=5)

        self.central_frame = Central_Frame(self, self.app, self.show_admin_frame)
        self.central_frame.grid(row=0, column=1, rowspan=3, sticky='nsew')
