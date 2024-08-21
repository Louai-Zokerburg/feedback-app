import customtkinter as ctk
from api.submit_feedback import submit_feedback


class FeedbackForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="Submit Your Feedback / Report an Issue")
        self.label.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Your Name")
        self.name_entry.pack(pady=10, fill="x")

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Your Email")
        self.email_entry.pack(pady=10, fill="x")

        self.feedback_entry = ctk.CTkTextbox(
            self, height=150, placeholder_text="Your Feedback / Issue"
        )
        self.feedback_entry.pack(pady=10, fill="x")

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

        self.response_label = ctk.CTkLabel(self, text="")
        self.response_label.pack(pady=10)

    def on_submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        feedback = self.feedback_entry.get("1.0", "end-1c")

        if name and email and feedback:
            self.submit_button.configure(state="disabled")
            self.response_label.configure(text="Submitting...")

            self.after(100, self.async_submit_feedback, name, email, feedback)
        else:
            self.response_label.configure(text="Please fill all fields.")

    def async_submit_feedback(self, name, email, feedback):
        response = submit_feedback(name, email, feedback)
        self.handle_response(response)

    def handle_response(self, response):
        self.submit_button.configure(state="normal")
        if response.status_code == 200:
            self.response_label.configure(
                text="Thank you for your feedback!", text_color="green"
            )
        else:
            self.response_label.configure(
                text="Failed to submit feedback.", text_color="red"
            )
