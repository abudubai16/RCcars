class AdminControl:
    start = True
    reset = True

    def __repr__(self):
        return f"Start: {self.start}, Reset: {self.reset}"


admin_control = AdminControl()
