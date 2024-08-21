import customtkinter as ctk
from gui.main_window import MainWindow

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme(
        "blue"
    )  # Themes: "blue" (default), "green", "dark-blue"

    app = MainWindow()
    app.mainloop()
