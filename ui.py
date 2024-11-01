import customtkinter
from tkextrafont import Font
import calc


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.sizeto(240, 330)  # Fenstergröße setzen
        self.title("Rechner")  # Fenstertitel setzen
        self.iconbitmap("resources/icon.ico")  # Fenstericon setzen

        customtkinter.set_default_color_theme("resources/orange.json")  # Farbschema setzen
        customtkinter.set_appearance_mode("dark")  # Erscheinungsmodus auf dunkel setzen
        
        Font(file="resources/Inter.ttf")  # Laden der Schriftart

        self.create_widgets()  # Widgets erstellen

    def clear_site(self):
        # Alle Widgets aus dem Fenster entfernen
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        # Maximale und minimale Fenstergröße setzen
        self.resizable(0,0)
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")

    def create_widgets(self):
        self.clear_site()  # Vorhandene Widgets entfernen
        
        self.__buttons = []
        for i in range(1, 10):
            # Zahlentasten erstellen und platzieren
            self.__buttons.append(customtkinter.CTkButton(self, text=str(i), command=lambda i=i: self.button_click(i), height=50, width=50, font=("Inter Black", 14), fg_color="#84817a"))
            self.__buttons[i-1].place(x=10 + ((i-1) % 3) * 55, y=105 + ((i-1) // 3) * 55)
        
        # Taste "0" erstellen und platzieren ( Unten )
        self.__buttons.append(customtkinter.CTkButton(self, text="0", command=lambda: self.button_click(0), height=50, width=50, font=("Inter Black", 14), fg_color="#84817a"))
        self.__buttons[-1].place(x=65, y=270)
        
        self.__dot = customtkinter.CTkButton(self, text=".", command=lambda: self.button_click("."), height=50, width=50, font=("Inter Black", 14))
        self.__dot.place(x=10, y=270)
        
        self.__backspace = customtkinter.CTkButton(self, text="←", command=lambda: self.__entry.delete(len(self.__entry.get())-1), height=50, width=50, font=("Inter Black", 14))
        self.__backspace.place(x=120, y=270)
        
        self.__equals = customtkinter.CTkButton(self, text="=", command=self.calculate, height=50, width=50, font=("Inter Black", 14))
        self.__equals.place(x=180, y=270)
        
        # Klammern und Modulus-Taste erstellen und platzieren ( Oben )
        self.__modulus = customtkinter.CTkButton(self, text="%", command=lambda: self.button_click("%"), height=50, width=50, font=("Inter Black", 14))
        self.__modulus.place(x=10, y=50)
        
        self.__open_bracket = customtkinter.CTkButton(self, text="(", command=lambda: self.button_click("("), height=50, width=50, font=("Inter Black", 14))
        self.__open_bracket.place(x=65, y=50)
        
        self.__close_bracket = customtkinter.CTkButton(self, text=")", command=lambda: self.button_click(")"), height=50, width=50, font=("Inter Black", 14))
        self.__close_bracket.place(x=120, y=50)
        
        # Operationstasten erstellen und platzieren ( Rechts )
        self.__add = customtkinter.CTkButton(self, text="+", command=lambda: self.button_click("+"), height=50, width=50, font=("Inter Black", 14))
        self.__add.place(x=180, y=50)
        
        self.__sub = customtkinter.CTkButton(self, text="-", command=lambda: self.button_click("-"), height=50, width=50, font=("Inter Black", 14))
        self.__sub.place(x=180, y=105)
        
        self.__mul = customtkinter.CTkButton(self, text="*", command=lambda: self.button_click("*"), height=50, width=50, font=("Inter Black", 14))
        self.__mul.place(x=180, y=160)
        
        self.__div = customtkinter.CTkButton(self, text="/", command=lambda: self.button_click("/"), height=50, width=50, font=("Inter Black", 14))
        self.__div.place(x=180, y=215)
        
        # Eingabefeld erstellen und platzieren
        self.__entry = customtkinter.CTkEntry(self, width=220, height=20, font=("Inter Black", 20))
        self.__entry.place(x=10, y=10)

        # Die Enter-Taste führt die Berechnung aus
        self.bind("<Return>", lambda e: self.calculate())

    def button_click(self, value):
        # Wert in das Eingabefeld einfügen
        entry = self.__entry.get()
        if entry == "Error":
            self.clear()

        self.__entry.insert("end", value)
        
    def clear(self):
        # Eingabefeld leeren
        self.__entry.delete(0, "end")
        
    def calculate(self):
        try:
            # Berechnung durchführen und Ergebnis anzeigen
            entry = self.__entry.get()
            result = None
            if entry == "":
                result = ""
            else:
                result = calc.calculate(entry)
                if result is None or result == float("inf") or result == float("-inf"):
                    raise Exception()

            self.clear()
            self.__entry.insert("end", str(result))
        except:
            # Fehlerbehandlung
            self.clear()
            self.__entry.insert("end", "Error")
        
            
