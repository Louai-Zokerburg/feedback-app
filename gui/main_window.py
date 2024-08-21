import customtkinter as ctk
from gui.feedback_form import FeedbackForm


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Feedback & Issue Report")
        self.geometry("500x400")
        self.iconbitmap("assets/icon.png")  # Set the path to your icon

        # Adding the feedback form
        self.feedback_form = FeedbackForm(self)
        self.feedback_form.pack(pady=20, padx=20, fill="both", expand=True)
