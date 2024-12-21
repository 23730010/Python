import unicodedata


class NVCommon:
    # Normalize function
    @staticmethod
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join(c for c in nfkd_form if not unicodedata.combining(c))

    # Function to validate numeric input
    @staticmethod
    def validate_number_input(action, value_if_allowed):
        if action == "1":  # 1 means insertion
            return value_if_allowed.isdigit()  # Allow only digits
        return True

    @staticmethod
    def show_center_of_window(root):
        # Center the popup on the screen
        root.update_idletasks()  # Ensure the geometry values are updated
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set geometry with calculated center position
        root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
