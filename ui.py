import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.sizeto(600, 400)
        self.title("Taschenrechner")

        customtkinter.set_default_color_theme("orange.json")  # color setter
        customtkinter.set_appearance_mode("dark")

        self.create_widgets()

    def clear_site(self):
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")

    def create_widgets(self):
        self.clear_site()
