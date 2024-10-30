import customtkinter
import calc


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.sizeto(240, 275)  # Fenstergröße setzen
        self.title("Rechner")  # Fenstertitel setzen

        customtkinter.set_default_color_theme("orange.json")  # Farbschema setzen
        customtkinter.set_appearance_mode("dark")  # Erscheinungsmodus auf dunkel setzen

        self.create_widgets()  # Widgets erstellen

    def clear_site(self):
        # Alle Widgets aus dem Fenster entfernen
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        # Maximale und minimale Fenstergröße setzen
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")

    def create_widgets(self):
        self.clear_site()  # Vorhandene Widgets entfernen
        
        self.__buttons = []
        for i in range(1, 10):
            # Zahlentasten erstellen und platzieren
            self.__buttons.append(customtkinter.CTkButton(self, text=str(i), command=lambda i=i: self.button_click(i), height=50, width=50))
            self.__buttons[i-1].place(x=10 + ((i-1) % 3) * 55, y=50 + ((i-1) // 3) * 55)
        
        # Taste "0" erstellen und platzieren
        self.__buttons.append(customtkinter.CTkButton(self, text="0", command=lambda: self.button_click(0), height=50, width=105))
        self.__buttons[-1].place(x=10, y=215)
        
        # Operationstasten erstellen und platzieren
        self.__add = customtkinter.CTkButton(self, text="+", command=lambda: self.button_click("+"), height=50, width=50)
        self.__add.place(x=180, y=50)
        
        self.__sub = customtkinter.CTkButton(self, text="-", command=lambda: self.button_click("-"), height=50, width=50)
        self.__sub.place(x=180, y=105)
        
        self.__mul = customtkinter.CTkButton(self, text="*", command=lambda: self.button_click("*"), height=50, width=50)
        self.__mul.place(x=180, y=160)
        
        self.__div = customtkinter.CTkButton(self, text="/", command=lambda: self.button_click("/"), height=50, width=50)
        self.__div.place(x=180, y=215)
        
        # Gleichheitszeichen-Taste erstellen und platzieren
        self.__equals = customtkinter.CTkButton(self, text="=", command=self.calculate, height=50, width=50)
        self.__equals.place(x=120, y=215)
        
        # Eingabefeld erstellen und platzieren
        self.__entry = customtkinter.CTkEntry(self, width=220)
        self.__entry.place(x=10, y=10)
        
    
    def button_click(self, value):
        # Wert in das Eingabefeld einfügen
        self.__entry.insert("end", value)
        
    def clear(self):
        # Eingabefeld leeren
        self.__entry.delete(0, "end")
        
    def calculate(self):
        try:
            # Berechnung durchführen und Ergebnis anzeigen
            result = calc.calculate(self.__entry.get())
            self.clear()
            self.__entry.insert("end", str(result))
        except:
            # Fehlerbehandlung
            self.clear()
            self.__entry.insert("end", "Error")
        
            
